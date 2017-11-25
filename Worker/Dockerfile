FROM python:3
WORKDIR /Users/dylan/Documents/College/CSY5/ScalableComputing/Cyclometric/Worker
ADD . /Users/dylan/Documents/College/CSY5/ScalableComputing/Cyclometric/Worker
EXPOSE 80
RUN pip install --trusted-host pypi.python.org -r requirements.txt
ENV NAME World

ADD worker.py /
CMD [ "python", "-u", "worker.py" ]
