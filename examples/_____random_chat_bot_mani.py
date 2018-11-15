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
waiting_list=[]


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
            checkUpdates(bot)
            
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def checkUpdates(bot):
    global update_id
    global waiting_list
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message : # your bot can receive updates without messages          
           
            #print(str(update))
            
            if update.message.text == 'add':  
                # Reply to the message
                
                update.message.reply_text("You are added to the chat pool. Everyone in the pool will see your username in the pool")

                temp_list=[update.message.chat.id, '@'+str(update.message.chat.username)]                
                
                waiting_list.append(temp_list)
                sendUpdates(bot)
                
            elif update.message.text == 'remove' :
            
                update.message.reply_text("You are successfully removed from random chat pool. You can enter the pool by sending 'add'")

                temp_list=[update.message.chat.id, '@'+str(update.message.chat.username)]                
                
                waiting_list.remove(temp_list)
                
                sendUpdates(bot)
                
            else :
                update.message.reply_text('Send "add" to participate in random chat. Send "remove" to remove yourself from the random chat pool')

def sendUpdates(bot) :
    print("sendUpdates")
    

    global waiting_list
    print(waiting_list)
    
  
   

    
    pool=""
    for user in waiting_list :  
            
            pool+=user[1]
            pool+='\n'
            
    for user in waiting_list :
        
        
        bot.send_message(user[0], text="Random chat pool :\n "+pool)
            
        
    
            


if __name__ == '__main__':
    main()
