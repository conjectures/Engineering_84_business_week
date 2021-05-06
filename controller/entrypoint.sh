# Add packages
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get install software-properties-common -y
sudo apt-get update -y

# Install packages
sudo apt-get install ansible awscli python3 python3-pip -y
# Install required pip modules
# pip3 install boto boto3

# Ansible file structure
mkdir -p /etc/ansible/group_vars/all
sudo cp /home/vagrant/provision/pass.yaml /etc/ansible/group_vars/all/
sudo cp /home/vagrant/provision/playbook.yaml /etc/ansible/

#ansible-playbook /etc/ansible/playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'
ansible-galaxy collection install ansible.posix

export ANSIBLE_HOST_KEY_CHECKING=False
export AWS_REGION=eu-west-1

