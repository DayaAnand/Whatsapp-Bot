from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        # get a cat quote
        r = requests.get('https://api.quotable.io/random')
        data = r.json()
        quote = f'{data["content"]} ({data["author"]})'
       
        msg.body(quote)
        responded = True
    if not responded:
        msg.body('sorry! , cannot retrieve a picture of cat with a quote')
    return str(resp)


if __name__ == '__main__':
    app.run()