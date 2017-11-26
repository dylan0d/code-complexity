FROM python:3
WORKDIR /Users/dylan/Documents/College/CSY5/ScalableComputing/Cyclometric/Manager
ADD . /Users/dylan/Documents/College/CSY5/ScalableComputing/Cyclometric/Manager
EXPOSE 80
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
ENV NAME World

ADD manager.py /
CMD [ "python3", "-u", "manager.py" ]
