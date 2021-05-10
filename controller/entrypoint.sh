#!/bin/bash
# Add packages
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get install software-properties-common -y
sudo apt-get update -y

# Install packages
sudo apt-get install ansible awscli python3 python3-pip -y

# Ansible file structure
sudo rm /etc/ansible/hosts /etc/ansible/ansible.cfg
sudo cp /home/ubuntu/controller/{playbook.yaml,ansible.cfg,hosts} /etc/ansible/

ansible-galaxy collection install ansible.posix

export ANSIBLE_HOST_KEY_CHECKING=False

ansible-playbook /etc/ansible/playbook.yaml -t ec2-configure -e "ansible_python_interpreter=/usr/bin/python3" 

ssh ubuntu@10.0.1.12 <<'EOF'
    cd app/
    export DB_HOST=mongodb://10.0.1.13:27017/posts?authSource=admin
    sudo killall node
    sudo pm2 kill
    sudo npm install
    node seeds/seed.js
    sudo pm2 start app.js --name app
EOF

# show time
date

