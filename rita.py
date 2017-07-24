
import os
import sys
import json
import requests
from flask import Flask, request,render_template
from secret_sauce.action_models import action_predict
from dsl import dsl
from templates.forms import InputForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '22334455'
@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])

def main():
    data = request.get_json() #messages from users are fetched
    if data["object"] == "page":
        for entry in data["entry"]:
            for message_event in entry["messaging"]:
                if message_event.get("message"):
                    sender_id = message_event["sender"]["id"] #facebook id of sender
                    recipent_id = message_event["recipient"]["id"] #bot id
                    message_text = message_event["message"]["text"] #message
                    reply = process_msg(message_text) #generating reply !
                    send_message(sender_id,reply) #replying

def process_msg(message_text):
    intent = action_predict(str(message_text)) #predicting action
    if intent != "none": #if the message is a command
        k = dsl(intent)
        reply = k.generate()
        return reply
    else: #if the message is just chitchat
        #seqtoseq model for normal chat to be implemented
        return "reply from seqtoseq model"


def send_message(recipient_id, message_text):

    params = {"access_token": os.environ["PAGE_ACCESS_TOKEN"]}
    headers = {"Content-Type": "application/json"}
    data = json.dumps({"recipient": {"id": recipient_id},"message": {"text": message_text}})
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)


@app.route('/test',methods=['GET', 'POST'])

def test():
    form = InputForm()
    if form.validate_on_submit():

        intent = action_predict(str(form.input_data.data))
        log(intent)
        if intent != "none":
            k = dsl(intent)
            reply = k.generate()
            log(reply)
            return render_template('index.html',reply = reply,form = form)
        else:
            #reply = seqtoseq(str(form.input_data.data)) will get there soon !
            reply = "sorry i didnt get that"
            return render_template('index.html',reply = reply,form = form)
    return render_template('index.html',form = form)

def log(message):
    if message:
       print(str(message))
       sys.stdout.flush()
    else:
       print("NULL")
       sys.stdout.flush()

if __name__ == '__main__':
    #app.debug = True
    app.run()
