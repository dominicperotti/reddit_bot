# converto_bot
-Reddit bot that converts USD amounts to other currencies

- Called by the prompt "currencyconvert: " (upper or lowercase) followed by a USD amount declared with a "$"

- Currently not backwards compatable

- Is set to run every 10mins via crontab

- I used voussoir's reply_bot as a template, but did not directly clone from it  https://github.com/voussoir/reddit/blob/master/ReplyBot/replybot.py

-Somebody submitted another currency conversion bot to /r/botwatch on Friday night, but I started working on this prior to that. I did not use that bot as a referecne, but it does use the same method of file i/o to store the comments read without a DB. Here's the source code for the other bot: https://github.com/falcon9857/Exchange/blob/master/Exchange.py  
