import itchat
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE])
def text_reply(msg):
    print(msg)
    return None


itchat.auto_login()
itchat.run()

print(itchat.get_friends())