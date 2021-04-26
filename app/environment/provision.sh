#!/bin/bash

# Run update command
sudo apt update -y

# Upgrade
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y
# Edit configuration file
sudo mv $HOME/app/app/default_nginx.bkp /etc/nginx/sites-available/default

sudo systemctl restart nginx.service

# Install nodejs required version and dependencies
sudo apt install python-software-properties -y
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt install nodejs -y

# Install npm with pm2 globally
sudo npm install pm2 -g

# Install app packages
sudo npm install $HOME/app/app
sudo node $HOME/app/app/seeds/seed.js

# Run application
npm start --prefix $HOME/app/app


