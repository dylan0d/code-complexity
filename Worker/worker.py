from flask import Flask
import os, socket, requests, time
import json

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname()), 200

def getWork():
    response = requests.get('http://192.168.1.15:1000/get_work').text
    num_list = json.loads(response)
    print (num_list)
    answer = sum(num_list)
    print (answer)
    print (socket.gethostname())
    requests.post('http://192.168.1.15:1000/answer', data = json.dumps(answer))
    time.sleep(5)

if __name__ == "__main__":
    print (requests.get('http://192.168.1.15:1000'))
    while(1):
        getWork()

