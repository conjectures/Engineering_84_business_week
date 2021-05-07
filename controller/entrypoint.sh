# Add packages
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get install software-properties-common -y
sudo apt-get update -y

# Install packages
sudo apt-get install ansible awscli python3 python3-pip -y
# Install required pip modules
# pip3 install boto boto3

# Ansible file structure
# sudo mkdir -p /etc/ansible/group_vars/all
# sudo cp /home/ubuntu/controller/pass.yaml /etc/ansible/group_vars/all/
sudo rm /etc/ansible/hosts /etc/ansible/ansible.cfg
sudo cp /home/ubuntu/controller/{playbook.yaml,ansible.cfg,hosts} /etc/ansible/

#ansible-playbook /etc/ansible/playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'
ansible-galaxy collection install ansible.posix

export ANSIBLE_HOST_KEY_CHECKING=False
export AWS_REGION=eu-west-1

# Remove old hosts file
# sudo rm /etc/ansible/hosts /etc/ansible/ansible.cfg
# Copy new one
# sudo cp /home/ubuntu/controller/hosts.txt /etc/ansible/hosts
# sudo cp /home/ubuntu/controller/ansible.cfg /etc/ansible/ansible.cfg
