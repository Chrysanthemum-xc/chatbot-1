import re
import chatbot.chatbot_core as core
import database


def doAITell():
    while True:
        str = input("USER :")
        if core.bye(str):
            print(core.sayBye())
            break
        core.processRequest(str)
