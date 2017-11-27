#pylint: disable=C0111, C0103, W0603
import shutil
import os
import socket
import time
import json
import requests
from radon.complexity import cc_visit
import git

lastUrl = ""

def getWork(): #ask for work
    response = requests.get('http://10.6.90.53:1000/get_work').text
    response = json.loads(response)

    try:
        repo, commit, index = response
    except ValueError:
        print(response)
        time.sleep(30)
        return

    clone(repo, commit)

    fileList = getFiles(str(socket.gethostname()))
    complexity = 0

    if fileList:
        for fileName in fileList:
            complexity += getCC(fileName)

    answer = {"c":complexity, "index":index}
    print(answer)
    requests.post('http://10.6.90.53:1000/answer', data=json.dumps(answer))


def clone(url, commit): #get required repo
    global lastUrl
    if not url == lastUrl:
        if os.path.isdir("./"+str(socket.gethostname())):
            shutil.rmtree(str(socket.gethostname()))
        git.Git().clone(url, str(socket.gethostname()))
        lastUrl = url
    repo = git.Git(socket.gethostname())
    repo.checkout(commit)

def getCC(filepath): #get cyclical complexity of file
    with open(filepath, "r") as myfile:
        data = myfile.read()
        # cc = cc_visit(data)
        # return sum(function[len(function)-1] for function in cc)
        try:
            cc = cc_visit(data)
            return sum(function[len(function)-1] for function in cc)
        except Exception:
            return 0

def getFiles(folder): #get files in repo to check
    fileList = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        if not '.git' in dirpath and not '/.' in dirpath:
            for filename in filenames:
                if not filename[0] is '.' and ".py" in filename:
                    fileList.append(dirpath+'/'+filename)
    return fileList

if __name__ == "__main__":
    print(requests.get('http://10.6.90.53:1000'))
    while 1:
        getWork()
