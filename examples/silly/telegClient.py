from telethon import TelegramClient,sync
import time
from mss import mss
import traceback

api_id = 250149
api_hash='898d3c607f66f9049a944ec8dfd7a23b'


try :

	client = TelegramClient('session_name', api_id, api_hash)
	client.start()

	while True :
	    time.sleep(1)
	    messages = client.get_messages('mani_google_bot')
	    if messages[0].message=='screenshot':
	        print("entered if")
	        with mss() as sct:
	            sct.shot()
	        client.send_file('mani_google_bot', "monitor-1.png")    
	    print("mani")

except :
	print ("exception happened")
	traceback.print_exc()
	input()

    

    
