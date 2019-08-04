# Zergs Twitchbot

The following is a twitchbot created primarily by the streamer [zerg](https://www.twitch.tv/zerg3rr) to be used in his twitch chat.

## Commands:
All commands are prefixed with `-`

When you are doing commands, if there are {} take those out when you 
do your command, ex. `-joinmessage Heil Gotdott` would set your 
joinmessage as Heil Gotdott

- ```-joinmessage {your message here}``` => This will set a join message for whenever you enter the channel (will cost 1000 points)
- ```-eightball``` => Ask ‘eightball’ yes or no questions simply by typing -eightball then your question
- ```-bm``` => bm yourself by typing -bm
- ```-feelgood``` => make yourself feel better after the bm
- ```-trivia``` => to do a trivia question
- ```-myid``` => for your own private ID which can be used to save update your data if you change names later on
- ```-joindate``` => to see the date the bot found you originally looking at the stream
- ```-hours``` => prints out your total hours
- ```-hours {gamename}``` => prints out the hours you’ve watched that game for
- ```-chatlines``` => show your total amount of chatlines in the stream
- ```-appsignup``` => if you know someone who might like the bot send them this link
- ```-compare``` {hours/points/chatlines username} => compare the amount of {keyword} you have total against your friend (this does not include offline chatlines)
- ```-top {hours/points/chatlines}``` => shows the top 10 for {keyword}
- ```-testme``` => the bot isnt always nice… beware
- ```-game``` => prints out what game we are playing
- ```-invite {username}``` => let the streamer know who invited you to the stream!
- ```-gn {##}``` => guess a random number, you get nothing if you win
- ```-eightball``` => works like a normal eightball
- ```-remove_joinmessage``` => removes a users joinmessage at no cost
- ```-update_id {old_uid}``` => Updates your old uid into your new UID
- ```-stats``` => Shows you your chatlines and hours for the last 30 days in stream

## Installation:
Install all requirements: `pip3 install -r requirements.txt`


## Usage:


## Todo:

- Freeze packages into a requirements.txt **IMPORTANT**
- Use F strings in DB calls to pervent SQLi **IMPORTANT**
- Add missing doctrings on all functions/methods
- Refactor the following functions: 
  - bot.py
    - steamers_pref
    - handle_response
    - timefunctions
  - botcommands.py
    - handle_commands
    - sql_commands.py
    - check_users_joindate
    - check_mods
  - merge_databases.py
    - copy_viewerdata
- Update readme with install and usage instructions.
- Merge changelogs directly with git releases and tags.

## Special Thanks:
To [Thukor](https://github.com/Thukor), and GreenMachine! for their contribution to this bot.
