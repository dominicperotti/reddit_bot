import time
import praw
from pprint import pprint

r = praw.Reddit('PRAW related-questions monitor by /u/_Daimin_ v 1.0. ' 'Url: https://praw.readthedocs.org/en/latest/' 'pages/writing_a_bot.html')

r.login()
already_done = []
prawWords = ['praw', 'reddit_api', 'mellort']

while True:
	subreddit = r.get_subreddit('learnpython') #change this to umw_cpsc for actual thing
	for submissions in subreddit.get_hot(limit = 10):
		op_text = submission.selftext.lower()
		has_praw = any(string in op_text for string in prawWords)
		#Test if has praw  question
		if submission.id not in already_done and has_praw:
			# write message to Daimon
			msg = '[PRAW related thread](%s)' % submission.short_link
			r.send_message('_Daimon_', 'PRAW Thread', msg)
			already_done.append(submission.id)
	time.sleep(1800) #do every 30mins
