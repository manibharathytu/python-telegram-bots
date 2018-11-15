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
            setUpChats(bot)
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
            if update.message.text == 'r':  
                # Reply to the message
                
                update.message.reply_text("Wait! I'm pulling out a chat mate for you")

                temp_list=[]
                temp_list.append(update.message.chat.id)
                temp_list.append('@'+update.message.chat.username)
                
                waiting_list.append(temp_list)
                
                
            else :
                update.message.reply_text('Type r to get random chat ')

def setUpChats(bot) :

    global waiting_list
    
    length=len(waiting_list)
    print(length)
    if length < 2 : #not enough ppl to match
        return
    
    if length % 2 == 0 :
        to_match_list=waiting_list
        waiting_list=[]
        
    else :
        to_match_list=waiting_list
        waiting_list=waiting_list[length-1:]
        to_match_list=to_match_list[:length-1]
        length-=1

    length=len(to_match_list)
    
    list1, list2=to_match_list[:int(length/2)],to_match_list[int(length/2):]

    for user1,user2 in zip(list1, list2) :   

        print("loop start")
        print(user1[0])
        bot.send_message(user1[0], text="Gotcha! You are mathced with "+user2[1] + ". You can ping first or wait for them to ping you.")
        bot.send_message(user2[0], text="Gotcha! You are mathced with "+user1[1] + ". You can ping first or wait for them to ping you.")
        print("loop end")
    
            


if __name__ == '__main__':
    main()
