from flask import Flask
import os
import socket
import json
import requests

numbers = [0,1,2,3,4,5,6,7,8,9]
done = False
index = 0
app = Flask(__name__)

@app.route("/get_work")
def send_work():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>I am a manager</b>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname()), 200

@app.route("/")
def hello():

    response = "I am the manager, ask me for work"
    return response, 200

if __name__ == "__main__":
    requests = requests.get('http://192.168.1.15:4000')
    print (requests)
    app.run(host='0.0.0.0', port=80)
