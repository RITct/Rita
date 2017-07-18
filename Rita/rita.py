
import json
from flask import Flask, request
from secret_sauce.models import predict_action
app = Flask(__name__)

@app.route('/', methods=['POST'])

def main():
    if request.method == 'POST':
        try:
            data = json.loads(request.data.decode('utf-8'))

        except (ValueError, TypeError, KeyError):
            return json.dumps({'label': 'error'})
        if data['label'] == "text":
            intent = predict_action(data['request'])
            if intent != "none":
                pass #actions to be implemented in dsl.py
            else:
                pass
               #seqtoseq model for normal chat to be implemented


@app.route('/test')

def testmain():
    pass
    
    #test user interface to be implemented

if __name__ == '__main__':
    app.debug = True
    app.run()
