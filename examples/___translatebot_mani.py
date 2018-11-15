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

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging
from lib_mani import translate
from multiprocessing.dummy import Pool as ThreadPool


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

    
    article_list=[]
   # lang_list=[['fr','français'],['es','español']]#,['de','Deutsch']]#,['ja','日本語'],['zh','中文'],['ar','العربية'], ['hi','हिन्दी'],['ru','русский'],['pt','português'] ]
    lang_list=['fr', 'es','de','pt', 'it','ja','zh','ar','hi','ru' ]
    
    language_list=['français', 'español', 'Deutsch', 'português', 'italiano', '日本語', '中文', 'العربية', 'हिन्दी', 'русский']
    image_url_list=['https://www.brainscape.com/blog/wp-content/uploads/2015/06/French.jpg',
               'https://cdn.viagogo.net/img/cat/4371/0/37.jpg',
               'http://eplaw.org/wp-content/uploads/2015/11/german-flag.jpg',
               'https://senhorcabo.com/wp-content/uploads/2017/08/brasil-portugal-696x432.jpg',
               'https://thumb1.shutterstock.com/display_pic_with_logo/937696/626745869/stock-vector-italy-background-design-italian-sticker-symbols-and-objects-626745869.jpg',
               'https://i1.wp.com/tamenal.com/wp-content/uploads/2015/10/1444817920748.jpg?zoom=2&resize=400%2C220',
               'https://www.brainscape.com/blog/wp-content/uploads/2015/06/French.jpg',
               'https://www.brainscape.com/blog/wp-content/uploads/2015/06/French.jpg',
               'https://www.brainscape.com/blog/wp-content/uploads/2015/06/French.jpg',
               'https://www.brainscape.com/blog/wp-content/uploads/2015/06/French.jpg']
    #global translated_list
    #translated_list=['a','f','f','f','f','f','f','f','f','ds']
    translate.set_text(query)
    
    pool = ThreadPool(4)
    translated_list = pool.map(translate.translate_to, lang_list)

    
    #print(translate.translate_to("fr"))   

    for num in range(0,len(lang_list)) :
        
        
        
        article=    InlineQueryResultArticle(
            id=uuid4(),
            title=language_list[num]+" - "+translated_list[num],
            input_message_content=InputTextMessageContent(
                translated_list[num]),
            thumb_url=image_url_list[num])

        
        
        article_list.append(article)
        
    return article_list
       


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater("493205833:AAFLALz0-J8TcFRq64u2julitn-xPPgHuH0")

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
