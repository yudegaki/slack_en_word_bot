from slackbot.bot import listen_to
from slackbot.bot import respond_to
import json,random

D = state = {}


def loadJSON():
    global D
    try:
        with open("./plugins/wordlist.json",mode = 'r') as f:
            D = json.load(f)
    except FileNotFoundError:
        print("Error:wordlist.json not found")


@respond_to('problem')
def getproblem(message):

    display_name = message.user['profile']['display_name']
    
    if(display_name not in state or state[display_name] == -1):
        index = random.randrange(len(D))

        state[display_name] = index
        message.send(D[index]['J Translation']) 
    else:
        index = state[display_name]
        message.send(D[index]['J Translation'])
    

@respond_to(r'^ans\s+\S.*')
def sendans(message):
    display_name = message.user['profile']['display_name']
    
    if(display_name not in state or state[display_name] == -1):
        message.send("問題が出題されていません")
    else:
        text = message.body['text']
        _, word = text.split(None,1)
        index = state[display_name]

        if(word == D[index]["Meanings"]):
            message.react("ac")
        else:
            message.react("wa")

        message.send("ans is " + D[state[display_name]]["Meanings"])
        state[display_name] = -1



@respond_to('state')
def resp(message):
    # 名前と表示名を取得する
    real_name = message.user['real_name']
    display_name = message.user['profile']['display_name']

    message.send('hello '+ real_name) 



