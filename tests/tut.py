import praw
import pprint

user_agent = ("Karma breakdown 1.0 by /u/_Daimon_ "
		"github.com/Damgaard/Reddit-Bots")
r = praw.Reddit(user_agent=user_agent)

user_name = "_Daimon_"
user = r.get_redditor(user_name)

thing_limit = 10
gen = user.get_submitted(limit=thing_limit)

karma_by_subreddit = {}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)

pprint.pprint(karma_by_subreddit)
