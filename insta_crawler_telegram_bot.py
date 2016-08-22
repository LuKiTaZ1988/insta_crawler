# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import listdir, system, path

import os
import logging
import ConfigParser

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


config = ConfigParser.RawConfigParser()
config.read('insta_crawler.cfg')

TOKEN = config.get('Section_Telegram', 'token')

# Define a few command handlers.
def start(bot, update):
    text = 'Hello! This bot is designed for stalking people by retreiving their images '+\
    "from their Instagram accounts.\nPlease use command /user username\n" +\
    "For example: /user emrata"
    bot.sendMessage(update.message.chat_id, text=text)

def user(bot, update):
    if len(update.message.text.split()) > 2:
        text = 'Bad usage, only one parameter admitted:\nTry /user emrata'
        bot.sendMessage(update.message.chat_id, text=text)
        return

    arg = update.message.text.split()[1]
    if os.system('python insta_crawler.py --profile {}'.format(arg)) != 0:
        text = 'Error while scrawling, maybe user does not exists:\nTry /user emrata'
        bot.sendMessage(update.message.chat_id, text=text)
        return

    img_path = "insta_crawler/{}/images/".format(arg)
    for f in listdir(img_path):
        bot.sendPhoto(chat_id=update.message.chat_id, photo=open(os.path.join(img_path,f), 'rb'))

def echo(bot, update):
    text = 'I dont understand:\nTry /user emrata'
    bot.sendMessage(update.message.chat_id, text=text)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("user", user))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
