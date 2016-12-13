#usr/bin/bash

sudo apt-get install python-setuptools python-dev build-essential -y

sudo apt-get -y install python-pip -y

sudo pip install -U boto -y

sudo pip install awscli -y

wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins -y

sudo apt-get install software-properties-common -y
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get update 
sudo apt-get install ansible -y

wget -qO- https://get.docker.com/ | sh