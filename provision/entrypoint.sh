# Add packages
sudo apt-add-repository ppa:ansible/ansible -y
sudo apt-get install software-properties-common -y
sudo apt-get update -y

# Install packages
sudo apt-get install ansible python3 python3-pip -y
# Install required pip modules
pip3 install boto boto3

# Ansible file structure
# ansible-vault create pass.yaml

