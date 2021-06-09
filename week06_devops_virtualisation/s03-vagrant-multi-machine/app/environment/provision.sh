#!/bin/bash

# Run update command
sudo apt update -y

# Upgrade
sudo apt upgrade -y

# Install nginx
sudo apt install nginx -y
# Edit configuration file
sudo sh -c "echo \"server {
    listen 80;

    server_name _;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }
}\" >  /etc/nginx/sites-available/default"
sudo systemctl restart nginx.service

# Install nodejs required version and dependencies
sudo apt install python-software-properties
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt install nodejs -y

# Install npm with pm2 globally
sudo npm install pm2 -g

# Install app packages
sudo npm install /home/vagrant/app/app
sudo node /home/vagrant/app/app/seeds/seed.js

# Run application
npm start --prefix /home/vagrant/app/app


