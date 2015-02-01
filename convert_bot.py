import time
import praw
import traceback
from pprint import pprint
from decimal import *

#Config Stuff
#BOT_USERNAME = ""
#BOT_PASSWORD = ""
USER_AGENT = 'Currency conversion bot by /u/dperotti v 1.0.' 'URL: https://github.com/dominicperotti/reddit_bot/tree/master'
SUBREDDIT = "umw_cpsc470Z"
KEYWORDS = ["currencyconvert:"]
already_done = []

#Conversion Rates to US dollar
EUR = Decimal(0.88324)
GBP = Decimal(0.66384)
CAD = Decimal(1.26605)
BTC = Decimal(0.00430)
JPY = Decimal(117.80)
AUD = Decimal(1.28660)
try:
	from bot_configs import *

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
				already_done.append(comment.id)
				#Get dollar amount and convert
				reply_text = ""
				comment_array = comment_text.split()
				#print "Found one! comment_array is: "
				#print comment_array
				for word in comment_array:
					if "$" in word and word.index("$") == 0:
						amount = word.replace("$", "")
						float_amount = Decimal(amount)
						eur_amount = str((float_amount * EUR).quantize(Decimal('.01'))).replace(".", ",")
						gbp_amount = str((float_amount * GBP).quantize(Decimal('.01')))
						cad_amount = str((float_amount * CAD).quantize(Decimal('.01')))
						btc_amount = str((float_amount * BTC).quantize(Decimal('.00001')))
						jpy_amount = str((float_amount * JPY).quantize(Decimal('1')))
						aud_amount = str((float_amount * AUD).quantize(Decimal('.01')))
						reply_text =  word + " conversions: \n\nAUD: " + aud_amount + "\n\nBTC: " + btc_amount + "\n\nCAD: " + cad_amount + "\n\nEUR: " + eur_amount + "\n\nGBP: " + gbp_amount + "\n\nJPY: " + jpy_amount	
						#comment.reply(reply_text)
						print "Reply text is : " + reply_text
		print "Done!"
	except Exception as error_message:
		print error_message


print "searching through comments"
while True:
	convert()
	time.sleep(1800)
