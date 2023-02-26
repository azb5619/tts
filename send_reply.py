from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from search_engine import toText
from gpt import generate_response
from weather import getImage, find_nearest

app = Flask(__name__)

def search(body):
    results = toText(body)
    b_split = body.split()
    if len(b_split) > 1 and b_split[-1].isdigit():
        return get_results(body, results)[int(b_split[-1])]
    return get_results(body, results)

def get_results(body, results):
    resp = MessagingResponse()
    string = "Results: \n"
    for i in range(len(results)):
        string += f"{i}: {results[i][0]}\n"
    resp.message(string)
    return str(resp)

def chatbot(body):
    resp = MessagingResponse()
    return str(resp)

def weather(body):
    resp = MessagingResponse()
    city = find_nearest(body)
    resp.message(city[0]).media(getImage(city))
    return str(resp)

@app.route("/", methods=['GET', 'POST'])
def query():
    body = str(request.values.get('Body', None))
    if '!c' in body:
            return chatbot(body[3:])
    elif '!w' in body:
            return weather(body[3:])
    elif '!s' in body:
            return search(body[3:])
    resp = MessagingResponse()
    resp.message("Use '!c' for chatbot, '!w' for weather, and '!s' for search")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=False)
