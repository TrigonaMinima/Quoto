Quoto
------------------

Simple application which displays a Quote on regular intervals of time.

##Features
- Same quote on a particular day  
- Random quote everyday  
- Quote fetched from my goodreads liked quotes
- Quoted displayed on a regular interval (3 hours interval)

##Tools Used
- Python 3.4
- PyQt 4
- feedparser (python module)

##How?
It creates a json file having the data of previous day. It then fetches the RSS feed of the liked quotes of mine from the Goodreads. Then selects a quote randomly and displays it.