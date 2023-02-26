from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from search_engine import toText
<<<<<<< HEAD
from gpt import generate_response
=======
from weather import getImage, find_nearest
>>>>>>> 625773d (implemented weather query)

app = Flask(__name__)

def search(body):
    body = request.values.get('Body', None)
    results = toText(body)
    get_results(body, results)
    body = request.values.get('Body', None)
    select_result(body, results)

def get_results(body, results):
    resp = MessagingResponse()
    string = "Results: \n"
    for i in range(len(results)):
        string += f"{i}: {results[i][0]}\n"
    resp.message(string)
    return str(resp)

def select_result(body, results):
    resp = MessagingResponse()
    return str(results[int(body)][1])

def chatbot(body, results):
    resp = MessagingResponse()
    return generate_response(resp)

def weather(body):
    resp = MessagingResponse()
    city = find_nearest(body)
    resp.message(body=city,
                 media_url=getImage(city))
    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def query_reply():
    body = request.values.get('Body', None)
    match body[:2]:
        case '!c':
            chatbot(body[2:])
        case '!w':
            weather(body[2:])
        case _:
            search(body[2:])

if __name__ == "__main__":
    app.run(debug=True)
