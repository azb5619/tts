from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    if body == 'hi':
        resp.message('yo')
    elif body == 'bye':
        resp.message('dueces')
    else:
        resp.message('sup')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
