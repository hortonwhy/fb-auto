from itertools import islice
from fbchat import Client
from fbchat.models import *
from getCookies import *

#consider using getpass for inputing the password
txt = open('message.txt','r')
message = [i.split(';') for i in txt]

loginTxt = open('login.txt','r')
loginInfo = [i.split(' ') for i in loginTxt]


class CustomClient(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        thread_ID = client.fetchThreadList()
        chat = client.fetchThreadMessages(thread_ID[0].uid) #most recent thread
        if len(chat) <= 2:
            client.send(Message(text =message[0][0]), thread_ID[0].uid, thread_type=ThreadType.USER)
        else:
                if chat[0].text == 'buying' and author_id != client.uid:
                    client.send(Message(text =message[0][1]), thread_ID[0].uid)
                elif chat[0].text == 'selling' and author_id != client.uid:
                    client.send(Message(text =message[0][2]), thread_ID[0].uid)

def main():

    session_cookies = openCookies()
    client = CustomClient(loginInfo[0][0],loginInfo[0][1], session_cookies=session_cookies)
    writeCookies(client.getSession())
    client.listen()


if __name__ == '__main__':
    main()

