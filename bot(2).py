from rubika.client import Bot
from  threading import Thread
from os import remove
import requests
import urllib

bot = Bot("app_name",auth="gagbocfevkbvnnftvrhrwugtdddasawv")
guid = "u0CrOci0542b2372d5a201dc7c846788"

list_message_seened = []

def indo():
    while True:
        try:
            chats_list:list = bot.getChatsUpdate()
            if chats_list != []:
                for chat in chats_list:
                    m_id = chat['object_guid'] + chat['last_message']['message_id']
                    if not m_id in list_message_seened:
                        access = chat['access']
                        if chat['abs_object']['type'] == 'User' and chat["object_guid"]!=guid:
                            text:str = chat['last_message']['text']
                            if 'SendMessages' in access and chat['last_message']['type'] == 'Text' and text.strip() != '':
                                text = text.strip()
                                if text.startswith("/start"):
                                    try:
                                        bot.sendMessage(chat['object_guid'],"سلام به اینستا دانلودر خوش آمدید \n اول در چنل زیر عضو شوید \n \n https://rubika.ir/X_Security \n سپس برای دانلود لینک خود را به صورت زیر ارسال کنید \n /download link",message_id=chat['last_message']['message_id'])
                                    except:
                                        print("error")
                                if text.startswith("/download "):
                                    try:
                                        bot.sendMessage(chat['object_guid'] , "در حال دانلود...",message_id=chat['last_message']['message_id'])
                                        
                                        url = requests.get("http://api.hajiapi.tk/instaDOWNLOAD/?url=" + text[10:])
                                        
                                        remote_url=url.json()['Results']['post'][0]
                                        
                                        print(remote_url)
                                        
                                        local_file = 'downloader.mp4'
                                        
                                        urllib.request.urlretrieve(remote_url, local_file)
                                        
                                        bot.sendDocument(chat['object_guid'] , 'downloader.mp4',message_id=chat['last_message']['message_id'])
                                        
                                        remove('downloader.mp4')

                                    except:
                                        print("error")
        
        except Exception as e:
            print(e)
            pass
            
while True:
    try:
        t1 = Thread(target=indo())
        t1.start()
    except:
        print("error")