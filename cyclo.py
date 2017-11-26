from radon.complexity import cc_rank, cc_visit
import git, os
def clone():
    git.Git().clone('https://github.com/dylan0d/Scalable-Computing.git', './new_folder')
    repo = git.Git("./new_folder")
    log = repo.log()
    print (log)
    lines = log.splitlines()
    commits = [lines[x*6].split()[1] for x in range(int(len(lines)/6)+1)]
    commits.reverse()
    print (commits)
    repo.checkout(commits[-1])

def getCC(filepath):
    with open (filepath, "r") as myfile:
        data=myfile.read()
        cc = cc_visit(data)
        print (sum(x[7] for x in cc))

def getFiles(folder):
    fileList = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        if not '.git' in dirpath and not '/.' in dirpath:
            for filename in filenames:
                if not filename[0] is '.':
                    print (dirpath+'/'+filename)
                    fileList.append(dirpath+'/'+filename)
    return fileList

if __name__ == "__main__":
    clone()
    getFiles('./')
    getCC("Worker/worker.py")