# Rita
Rita a.k.a RIT-assistant is the virtual assistant of RIT.

# Get the code
clone the repostory with
```
git clone https://github.com/RITct/Rita.git
```

# You need 
* [Python](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=0ahUKEwiI8POYnZjVAhVDW5QKHfTCC0cQFgghMAA&url=https%3A%2F%2Fwww.python.org%2F&usg=AFQjCNHtL9dpRTydwE89-fkyoeBWw_Ih6g)
* [PyTorch](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjR0dTMnJjVAhUBLZQKHTv2DRkQFgglMAA&url=http%3A%2F%2Fpytorch.org%2F&usg=AFQjCNEXSfCCJoYl_S4Utq27TyMxwyWZsg)
* [Flask](https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiR-qGLnZjVAhWMQpQKHTAvCR4QFgglMAA&url=http%3A%2F%2Fflask.pocoo.org%2F&usg=AFQjCNHCF6gYMbnkUKtJl-u3lzTeLt-61A)
* [Requests](http://docs.python-requests.org/en/master/)
# How to run
The web app should be deployed to the server for running it in fb messenger app.
A local interface can be run after implementing it(see task 3) like this
```
python rita.py
```
# Working
Currently building Rita as a facebook messenger bot in [python](www.python.org) [flask](flask.pocoo.org) based on this [tutorial](https://blog.hartleybrody.com/fb-messenger-bot/).

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
This is how things work inside process_msg(),
```
def process_msg(message_text):
    intent = predict_action(str(message_text)) #predicting action
    if intent != "none": #if the message is a command
        k = dsl(intent)
        reply = k.generate()
        return reply
    else: #if the message is just chitchat
        #seqtoseq model for normal chat to be implemented
        return "reply from seqtoseq model"

```
The predict_action() function output an action to be performed or "none" if no intent recognised. If intent is found then action is executed in dsl.py and a reply is generated. If predict_action() return "none", that means its a normal conversation like, 
"hello how are you ?"
Another model called seqtoseq will generate a reply for the question. 

We use two neural network models in Rita
## 1. Intent Recognition model
```
intent = predict_action(str(message_text))
```
Which will predict the action to be done by the bot from the message.
For example say "tell me about RIT", for this question bot may reply with link to RIT website.
This is an example tutorial for how to build an [intent recogniser](https://github.com/GopikrishnanSasikumar/Text_Classifier-pytorch).
The dataset used to train this model is stored in
```
action_dataset.json
```
## Note:whats inside it now is just stupid. See the task 1  

The intent recognition model can be trained by running
```
python action_train.py
```
## 2. SeqtoSeq model
This model is used for implementing normal conversations for questions like 
"hello how are you ?"
Its a neural network model that will translate the question to answer like this.
![alt text](https://camo.githubusercontent.com/242210d7d0151cae91107ee63bff364a860db5dd/687474703a2f2f6936342e74696e797069632e636f6d2f333031333674652e706e67)

SeqtoSeq model in pytorch can be implemented like [this](http://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html#sphx-glr-intermediate-seq2seq-translation-tutorial-py).
# Tasks
1. Make a list of actions to be performed by Rita.Create dataset for those actions inside action_dataset.json in the form like this,
```
"intent": "website","sentence": "open college website"
"intent":"website", "sentence":"show me RIT website"
"intent":"website", "sentence":"give me more information"
"intent":"website", "sentence":"tell me more about RIT"
```
2. Implement seqtoseq model. This need large dataset of question-answers. Plan is to deploy the bot with action recognition model and collect the questions people ask for making seqtoseq dataset.      
   
3. Make an interface to test the bot locally. That code goes here.
```
@app.route('/test')
def testmain():
    pass
    #test user interface to be implemented
```
The interface should have a dialogue boxes to take input message and display the reply.
This part of the [tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates) helps to do that.


## See you on Ritu :heart:
