import time
import praw
from pprint import pprint

r = praw.Reddit('Currency conversion bot by /u/dperotti v 1.0.' 'URL: https://github.com/dominicperotti/reddit_bot/tree/master')

r.login()
already_done = []
keyWords = ['CurrencyConversion:']
