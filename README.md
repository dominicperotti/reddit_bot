# convert_bot
- Reddit bot that converts USD amounts to other currencies

- Called by the prompt "currencyconvert: " (upper or lowercase) followed by a USD amount declared with a "$"

- Currently not backwards compatable

- Is set to run every 10mins via crontab

- I used voussoir's reply_bot as a template, but did not directly clone from it  https://github.com/voussoir/reddit/blob/master/ReplyBot/replybot.py

- Somebody submitted another currency conversion bot to /r/botwatch on Friday night, but I started working on this prior to that. I did not use that bot as a referecne, but it does use the same cheating method of file i/o to store already_done without a DB. Here's the source code for the other bot: https://github.com/falcon9857/Exchange/blob/master/Exchange.py  

# Sample Input/Output
- Input: "CurrencyConvert: $15.00"
- Output: "$15.00 conversions:
AUD: 19.30
BTC: 0.06450000
CAD: 18.99
EUR: 13,25
GBP: 9.96
JPY: 1767
MXN: 224.64"

- Input: "currencyconvert: $26.12"
- Output: "$26.12 conversions:
AUD: 33.61
BTC: 0.11231600
CAD: 33.07
EUR: 23,07
GBP: 17.34
JPY: 3077
MXN: 391.17"
