To run this file, run docker-compose up in the Manager folder. Once the flask
app is running, run docker-compose up in the Worker folder. The number of workers
created is determined by the docker.yml file. Comment out any workers that are not
required.

This program calculates the cyclomatic complexity of the DeblurGAN repo on 
github.com. It creates a manager which clones the repo and creates a list of commit 
hashes. Any number of workers can request work from the manager, which will send
it the url of the repo, the commit to be analysed and the index of that commit
(first commit is index 0, second is index 1 etc). The worker will then clone the 
provided repo (if not already cloned from a previous request), checkout that 
commit and calculate the complexity of each file. It returns the complexity and
the index so that the manager knows what commit the complexity belongs to. The
manager keeps track of which commits have been analysed and which haven't, so 
if a worker doesn't return its assigned commit for some reason it will be reassigned
at a later point.

graph.png shows how the complexity of the repo evolves over time

final graph.png shows how the different number of workers affects the runtime of 
the program. This graph excludes the time taken to clone the repo as each 
worker was runing on the same laptop, so if one worker takes Y seconds to clone the 
repo, X workers will take X*Y seconds as each worker needs their own copy. 

The graph is relatively flat, which is due to them running on the same machine.