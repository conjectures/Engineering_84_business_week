#! /bin/bash

echo "$1 " > /tmp/vault_pass

ansible-playbook /etc/ansible/provision_playbook.yaml \
    --vault-password-file /tmp/vault_pass \
    -e "ansible_python_interpreter=/usr/bin/python3" \
    -t ec2-create,ec2-controller

echo -e "\nSSH Infon\n"

ls /home/vagrant/.ssh
cat /home/vagrant/.ssh/config

echo -e "\nConnecting to controller...\n\n"

ssh -F /home/vagrant/.ssh/config controla '. /home/ubuntu/controller/entrypoint.sh'




