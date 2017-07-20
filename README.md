# Rita
Rita a.k.a RIT-assistant is the virtual assistant of RIT.

# Get the code
clone the repostory with
```
git clone https://github.com/RITct/Rita.git
```

# You need 
* [python](www.python.org)
* [pytorch](pytorch.org)
* [flask](flask.pocoo.org)

# Working
Currently building Rita as a facebook messenger bot in [python](www.python.org) [flask](flask.pocoo.org) based on this tutorial,
```
https://blog.hartleybrody.com/fb-messenger-bot/
```
Message user send is fetched.
```
data = request.get_json()
```
This will be in json format as send by [facebook API](https://developers.facebook.com/docs/messenger-platform/webhook-reference/message).
```
{
  "sender":{
    "id":"USER_ID"
  },
  "recipient":{
    "id":"PAGE_ID"
  },
  "timestamp":1458692752478,
  "message":{
    "mid":"mid.1457764197618:41d102a3e1ae206a38",
    "text":"hello, world!",
    "quick_reply": {
      "payload": "DEVELOPER_DEFINED_PAYLOAD"
    }
  }
}    
```
The message is parsed and extracted.
```
message_text = message_event["message"]["text"]
```
This message is processed and reply is generated using neural networks.
```
reply = process_msg(message_text)
```
We use two neural network models in Rita
## 1. Intent Recognition model
Which will predict the action to be done by the bot from the message.
For example say "tell me about RIT", for this question bot may reply with link to RIT website.
```
intent = predict_action(str(message_text))
```
## 2. SeqtoSeq model
This model is used for implementing normal conversations.
Its a neural network model that will translate the question to answer like this.
![alt text](https://camo.githubusercontent.com/242210d7d0151cae91107ee63bff364a860db5dd/687474703a2f2f6936342e74696e797069632e636f6d2f333031333674652e706e67)



## See you on Ritu :heart:
