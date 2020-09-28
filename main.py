from slackbot.bot import Bot
import json
from plugins.resp import loadJSON




def main():
    bot = Bot()
    bot.run()

if __name__ == '__main__':
    loadJSON()
    main()
