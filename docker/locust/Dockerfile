FROM ubuntu:16.04

RUN apt-get -y update
RUN apt-get install -y python-pip
RUN apt-get update -y
RUN pip install locustio
RUN apt-get install -y python-zmq
RUN apt-get install -y git
RUN apt-get -y update

RUN git clone https://github.com/otgcjm/devopstest.git

EXPOSE 8089
EXPOSE 5557

WORKDIR /devopstest/load-test

ENTRYPOINT ["locust", "-f", "event_collector.py"]