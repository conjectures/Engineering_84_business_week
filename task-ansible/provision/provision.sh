#!/bin/bash

# Add packages
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get install software-properties-common -y
sudo apt-get update -y

# Install packages
sudo apt-get install ansible awscli python3 python3-pip -y
# Install required pip modules
pip3 install boto boto3

# Ansible file structure
mkdir -p /etc/ansible/group_vars/all
sudo cp /home/vagrant/provision/pass.yaml /etc/ansible/group_vars/all/
sudo cp /home/vagrant/provision/{provision_playbook.yaml,configure_playbook.yaml,ansible.cfg} /etc/ansible/
cp /home/vagrant/provision/ansible.cfg /home/vagrant/.ansible.cfg

#ansible-playbook /etc/ansible/playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'
ansible-galaxy collection install ansible.posix

# Add env vars
export ANSIBLE_HOST_KEY_CHECKING=False
export AWS_REGION=eu-west-1
echo $ANSIBLE_HOST_KEY_CHECKING
echo $AWS_REGION


echo -e "Host *\n  ForwardAgent yes" | sudo tee /home/vagrant/.ssh/config
# echo -e "Hosts"


echo "$1 " > /tmp/vault_pass

ansible-playbook /etc/ansible/provision_playbook.yaml \
    --vault-password-file /tmp/vault_pass \
    -e "ansible_python_interpreter=/usr/bin/python3" \
    --tags=ec2-create,ec2-controller,ec2-ssh

# add to known hosts

echo -e "\nSSH Debug\n"
cat /home/vagrant/.ssh/config

echo -e "\nConnecting to controller...\n\n"
ssh -F /home/vagrant/.ssh/config controla '. /home/ubuntu/controller/entrypoint.sh'

cat /home/vagrant/myhosts.txt

# sudo rm -f /home/vagrant/.ssh/config

