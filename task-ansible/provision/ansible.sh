#! /bin/bash

echo "$1 " > /tmp/vault_pass

sudo ansible-playbook /etc/ansible/provision_playbook.yaml \
    --vault-password-file /tmp/vault_pass \
    -e "ansible_python_interpreter=/usr/bin/python3" \
    --tags=ec2-create,ec2-controller,ec2,ec2-ssh


echo -e "\nSSH Debug\n"
cat /home/vagrant/.ssh/config

echo -e "\nConnecting to controller...\n\n"
ssh -F /home/vagrant/.ssh/config controla '. /home/ubuntu/controller/entrypoint.sh'

cat /home/vagrant/myhosts.txt

sudo rm -f /home/vagrant/.ssh/config
