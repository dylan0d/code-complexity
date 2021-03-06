#pylint: disable=C0111, C0103, W0603
import json
import shutil
import matplotlib
from flask import Flask, request
import git
matplotlib.use('Agg')
import matplotlib.pyplot as plt



repoUrl = 'https://github.com/KupynOrest/DeblurGAN.git'
repoName = "./managerRepo"

commitList = [] #list of commits
complexityList = [] #list of corresponding complexities
completeList = [] #list of commits that have been calculated
index = 0 #next commit to check
app = Flask(__name__)

@app.route("/answer", methods = ['POST']) #to return answer
def incorporate():
    print("received answer")
    response = (json.loads(request.data))
    print(response)
    global complexityList
    global completeList
    complexityList[response['index']] = response['c']
    completeList[response['index']] = True

    if all(completeList):
        f, ax = plt.subplots(1)
        xdata = range(len(complexityList))
        ydata = complexityList
        plt.ylabel('Cyclical Complexity')
        plt.xlabel('Commit Number')
        ax.plot(xdata, ydata)
        ax.set_ylim(ymin=0)

        plt.savefig("graph.png")

    print(complexityList)
    return "thank you", 200

@app.route("/get_work") #to ask for work to do
def send_work():
    global index
    global repoUrl
    global completeList
    global complexityList
    print(index)
    if not all(completeList):
        response = [repoUrl, commitList[index], index]
        index += 1
        index = index%len(commitList)
        while completeList[index%len(commitList)]:
            index += 1
            index = index%len(commitList)

    else:
        response = "No more work go to sleep"

    return json.dumps(response), 200

@app.route("/") #if you want to check that manager is up
def hello():
    response = "I am the manager, ask me for work"
    return response, 200

def setup(): #get list of commits in repo
    global repoUrl
    git.Git().clone(repoUrl, repoName)
    repo = git.Git(repoName)
    log = repo.log()
    lines = log.splitlines()
    commits = []
    for x in lines:
        if x[:6] == "commit":
            commits.append(x.split()[1])
    commits.reverse()

    global complexityList
    global completeList
    complexityList = [0 for x in commits]
    completeList = [False for x in commits]
    shutil.rmtree(repoName)

    return commits

if __name__ == "__main__":
    commitList = setup()
    app.run(host='0.0.0.0', port=80)
