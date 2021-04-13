#!/bin/bash

# Run update command
sudo apt update -y

# Upgrade
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y

# Install nodejs required version and dependencies
sudo apt install python-software-properties
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt install nodejs -y

# Install npm with pm2 globally
sudo npm install pm2 -g

# Install app packages
sudo npm install app/app

# Add db environment vars
export DB_HOST=192.168.10.101:27017
# Run application
npm start --prefix /home/vagrant/app/app


