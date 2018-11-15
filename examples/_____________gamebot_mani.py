#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Bot to reply to Telegram messages.

This is built on the API wrapper, see echobot2.py to see the same example built
on the telegram.ext bot framework.
This program is dedicated to the public domain under the CC0 license.
"""
import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep


update_id = None


def main():
    """Run the bot."""
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('546684347:AAE_TO7s9hraDKHm2Nz8PxEKeMyvJOzv8ow')

    # get the first pending update_id, this is so we can skip over it in case
    # we get an "Unauthorized" exception.
    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    """Echo the message the user sent."""
    global update_id
    
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        print(update.callback_query)
        print(update.callback_query.game_short_name)
        
        update_id = update.update_id + 1
        
        #if update.message:  # your bot can receive updates without messages
            # Reply to the message
        page_url="https://manibharathytu.github.io/my_website/game.html"
        if update.callback_query.game_short_name == "Obstacle_2D" :    
            page_url="https://manibharathytu.github.io/my_website/game.html"
            print("entered if")

        elif update.callback_query.game_short_name == "html_test_game" :    
            page_url="https://manibharathytu.github.io/my_website/test.html"
            print("entered else")

        elif update.callback_query.game_short_name == "video_chat_mani" :    
            page_url="https://appear.in/mani"
            print("entered else")


        

        update.callback_query.answer(url=page_url)


if __name__ == '__main__':
    main()
