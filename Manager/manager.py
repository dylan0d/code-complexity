from flask import Flask, request
from radon.complexity import cc_rank, cc_visit
import os
import socket
import json
import requests
import git
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

repoUrl = 'https://github.com/KupynOrest/DeblurGAN.git'
repoName = "./managerRepo"

commitList = []
complexityList = []
completeList = []
done = False
index = 0
app = Flask(__name__)

@app.route("/answer", methods = ['POST'])
def incorporate():
    print ("received answer")
    response = (json.loads(request.data))
    print (response)
    global complexityList
    global completeList
    complexityList[response['index']] = response['c']
    completeList[response['index']] = True

    if all(completeList):
        plt.ylabel('some numbers')
        plt.plot(complexityList)
        plt.savefig('graph.png')

    print (complexityList)
    return "thank you", 200

@app.route("/get_work")
def send_work():
    global index
    global repoUrl
    global completeList
    global complexityList
    print (index)
    if not all(completeList):
        response = [repoUrl, commitList[index], index]
        index+=1
        index = index%len(commitList)
        while completeList[index%len(commitList)]:
            index +=1
            index = index%len(commitList)

    else:
        response = "No more work go to sleep"

    return json.dumps(response), 200

@app.route("/")
def hello():
    response = "I am the manager, ask me for work"
    return response, 200

def setup():
    global repoUrl
    git.Git().clone(repoUrl, repoName)
    repo = git.Git(repoName)
    log = repo.log()
    lines = log.splitlines()
    commits = []
    for x in lines:
        if "commit" == x[:6]:
            commits.append(x.split()[1])
    commits.reverse()

    global complexityList
    global completeList
    complexityList =  [0 for x in commits]
    completeList = [False for x in commits]
    return commits

if __name__ == "__main__":
    commitList = setup()
    print (commitList)
    app.run(host='0.0.0.0', port=80)
