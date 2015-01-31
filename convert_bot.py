import time
import praw
import traceback
from pprint import pprint

#Config Stuff
BOT_USERNAME = ""
BOT_PASSWORD = ""
USER_AGENT = 'Currency conversion bot by /u/dperotti v 1.0.' 'URL: https://github.com/dominicperotti/reddit_bot/tree/master'
SUBREDDIT = "umw_cpsc470Z"
KEYWORDS = ["currencycovert"]
already_done = []

#Conversion Rates to US dollar
EUR = 0.88324
GBP = 0.66384
CAD = 1.26605
BTC = 0.00430
JPY = 117.80
AUD = 1.28660
try:
	import bot_configs
	BOT_USERNAME = bot_configs.getUsername()
	BOT_PASSWORD = bot_configs.getPassword()

except ImportError:
	pass
	
r  = praw.Reddit(USER_AGENT)
#r.login("BOT_USERNAME", "BOT_PASSWORD") 
subreddit = r.get_subreddit(SUBREDDIT)


def convert():
	try:
		all_comments = subreddit.get_comments(limit=None)
		for comment in all_comments:
			comment_text = comment.body.lower()
			contains_keyword= any(string in comment_text for string in KEYWORDS)
			if contains_keyword and str(comment.author) != BOT_USERNAME and comment.id not in already_done:
				already_done.add(comment.id)
					#Get dollar amount and convert
					#reply_text = ""
					#comment.reply(reply_text)
				print "FOund something in " + comment.id
			else:
				print "Nothing in " + comment.id
		print "Done!"
	except Exception as error_message:
		print error_message


print "searching through comments"
while True:
	convert()
	time.sleep(1800)
