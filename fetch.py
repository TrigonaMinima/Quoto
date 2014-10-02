import feedparser
import datetime
import json
from random import randint
import os.path

# Give link of the rss feed of the user's liked quotes.
url_base = "https://www.goodreads.com/quotes/list_rss/12149311-shivam?page="
# File with the local data in the json format.
local_file = "local.json"


def check_date(prev):
    """
    Returns the difference between todays date & 'prev' date.
    """
    today = datetime.date.today()
    if prev:
        prev = prev.split('-')
        prev = datetime.date(int(prev[0]), int(prev[1]), int(prev[2]))
        return (today - prev).days, str(today)

    return 100, str(today)


def local(local_data, data, page):

        quotes = []
        quotes.append(local_data['pre_quo2'])
        quotes.append(local_data['pre_quo1'])

        # Randomly selecting a quote.
        quote_num = randint(1, local_data['page' + str(page)])
        quote = data.entries[quote_num-1].description

        # If the quote selected has already been used in past 2 days then a new
        # one is selected.
        while quote in quotes:
            quote_num = randint(1, local_data['page' + str(page + 1)])
            quote = data.entries[quote_num].description

        # Changing the local data.
        local_data['pre_quo2'] = local_data['pre_quo1']
        local_data['pre_quo1'] = local_data['today_quo']
        local_data['today_quo'] = quote

        with open(local_file, 'w') as f:
            json.dump(local_data, f, indent=4)

        return quote


def quote(local_data):
    """
    Returns a random quote which does not match with the previous 2 quotes.
    """
    up_date = local_data['update']
    last_date = local_data['date']
    chk_up, local_data['date'] = check_date(up_date)
    chk, local_data['date'] = check_date(last_date)
    quote = ''

    if chk_up >= 30:
        local_data['update'] = local_data['date']
        count = 1
        url = url_base + str(count)
        data = feedparser.parse(url_base + str(count), 'utf-8')
        temp_data = data
        while data['entries']:
            local_data['page' + str(count)] = len(data['entries'])
            count += 1
            temp_data = data
            url = url_base + str(count)
            data = feedparser.parse(url)
        local_data['pages'] = count - 1

        quote = local(local_data, temp_data, count - 1)

    elif chk > 0 or local_data['today_quo'] == "":
        # Randomly select a page and fetch its rss feed from goodreads.
        page = randint(1, local_data['pages'])
        data = feedparser.parse(url_base + str(page))

        quote = local(local_data, data, page)

    else:
        quote = local_data['today_quo']

    return quote


def main():

    local_data = {}

    if not os.path.exists(local_file):
        with open(local_file, 'w') as f:
            local_data = {
                "date": "",
                "update": "",
                "pre_quo1": "",
                "pre_quo2": "",
                "today_quo": ""
            }
            json.dump(local_data, f, indent=4)

    # File reading.
    with open(local_file, "r") as f:
        local_data = json.load(f)

    # returns a random quote from the user's liked quotes
    return quote(local_data)

if __name__ == "__main__":
    print(main())
    # print(quote())
