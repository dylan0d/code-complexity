from radon.complexity import cc_rank, cc_visit
import git
def clone():
    git.Git().clone('https://github.com/dylan0d/Scalable-Computing.git')
    repo = git.Git("./Scalable-Computing")
    log = repo.log()
    print (log)
    lines = log.splitlines()
    commits = [lines[x*6].split()[1] for x in range(int(len(lines)/6)+1)]
    commits.reverse()
    print (commits)
def getCC(filepath):
    with open (filepath, "r") as myfile:
        data=myfile.read()
        cc = cc_visit(data)
        print (sum(x[7] for x in cc))

if __name__ == "__main__":
    clone()
    getCC("Worker/worker.py")