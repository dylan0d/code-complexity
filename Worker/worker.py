from flask import Flask
from radon.complexity import cc_rank, cc_visit
import shutil
import os, socket, requests, time
import json
import git

app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname()), 200

def getWork():
    response = requests.get('http://192.168.1.15:1000/get_work').text
    response = json.loads(response)
    repo, commit, index = response 

    clone(repo, commit)

    fileList = getFiles(str(socket.gethostname()))
    complexity = 0
    
    if fileList:
        for fileName in fileList:
            complexity+= getCC(fileName)

    answer = {"c":complexity, "index":index}
    requests.post('http://192.168.1.15:1000/answer', data = json.dumps(answer))
    shutil.rmtree(str(socket.gethostname()))
    #time.sleep(1)

def clone(url, commit):
    git.Git().clone(url, str(socket.gethostname()))
    repo = git.Git(socket.gethostname())
    repo.checkout(commit)

def getCC(filepath):
    with open (filepath, "r") as myfile:
        data=myfile.read()
        # cc = cc_visit(data)
        # return sum(function[len(function)-1] for function in cc)
        try:
            cc = cc_visit(data)
            return sum(function[len(function)-1] for function in cc)
        except Exception:
            return 0

def getFiles(folder):
    fileList = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        if not '.git' in dirpath and not '/.' in dirpath:
            for filename in filenames:
                if not filename[0] is '.' and ".py" in filename:
                    fileList.append(dirpath+'/'+filename)
    return fileList

if __name__ == "__main__":
    print (requests.get('http://192.168.1.15:1000'))
    while(1):
        getWork()