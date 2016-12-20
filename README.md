# Dockerized-Locust

First, you need a linux machine, install these applications:

 1. Python Pip
 2. Boto - AWS Command Line Interface
 3. Jenkins
 4. Ansible
 5. Docker

Then, execute these commands:

 - Enter your AWS credentials: aws configure
 - Add your AWS pem file, and execute: chmod 400 *.pem
 - Make jenkins user admin: visudo => jenkins ALL=(ALL) NOPASSWD: ALL (add bottom line)
 - Add jenkins user to docker group: usermod -aG docker jenkins
 - Add ec2.py as an ansible hosts file, and ec2.ini to the same directory with hosts file
 - Add: host_key_checking=false to the defaults section in ansible.cfg
 - For temp docker image, create a directory and give jenkins user to write permisson: chown -R jenkins folder_path
