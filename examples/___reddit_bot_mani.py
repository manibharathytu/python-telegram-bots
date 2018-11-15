#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from uuid import uuid4

from telegram.utils.helpers import escape_markdown

from telegram import InlineQueryResultArticle,InlineQueryResultPhoto, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
from lib_mani import GoogSearch




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query 
    
    results = get_result(query)    

    update.inline_query.answer(results)

    

def get_result(query):

    print("get result starts")
    urls_list, titles_list = GoogSearch.search(query + " reddit")
    
    reddit_urls_list = []
    reddit_titles_list = []
    for url,title in zip(urls_list,titles_list) :
        if "reddit.com" in url :
            
            reddit_urls_list.append(url)
            reddit_titles_list.append(title)
            
    print("goog query finished")

    
    article_list=[]
  


    for url,title_text in zip(reddit_urls_list, reddit_titles_list) :
        
        
        #title_text=url[url.rfind('com/')+4:]
       # title_text=title_text.replace("-", " ")
        #if title_text is "" :
           # title_text="Reddit"
        
        article=    InlineQueryResultArticle(
            id=uuid4(),            
            title=title_text,
            input_message_content=InputTextMessageContent(
                url),
            thumb_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRk3Lw8vgP7FFcGEDC2UP1pCWalBsn8PE_KSOcsURi0n0DzbDtT")

        
        
        article_list.append(article)
        
    return article_list
       


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("545237553:AAHEBVaqB72sGE5W6wCdYgrbAhPyefl3tvE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
