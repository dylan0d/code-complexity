from flask import Flask, request
import os
import socket
import json
import requests

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
done = False
index = 0
answer = 0
app = Flask(__name__)

@app.route("/answer", methods = ['POST'])
def incorporate():
    print ("received answer")
    number = (json.loads(request.data))
    global answer
    answer += number
    print (answer)
    return "thank you", 200

@app.route("/get_work")
def send_work():
    global index
    print (index)
    if index < len(numbers):
        response = [numbers[index]]
        index += 1
        response.append(numbers[index])
        index += 1
    else:
        response = "No more work go to sleep"
    return json.dumps(response), 200

@app.route("/")
def hello():

    response = "I am the manager, ask me for work"
    return response, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
