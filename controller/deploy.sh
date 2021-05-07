#! /bin/bash

echo -e "\nConnecting to application server...\n\n"
ssh -o StrictHostKeyChecking=no ubuntu@10.0.1.12 '. $HOME/app_env/provision.sh'
