from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from search_engine import toText

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    response = toText(body)
    string = ""
    for i in range(len(response)):
        string += f"{i}: {response[i][0]}\n"
    resp.message(string)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
