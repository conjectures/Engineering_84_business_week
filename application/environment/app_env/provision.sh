#!/bin/bash

# Update the sources list
sudo apt-get update -y

# upgrade any packages available
sudo apt-get upgrade -y


# install git
sudo apt-get install git -y

# install nodejs
sudo apt-get install python-software-properties -y
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install nodejs -y

# install pm2
sudo npm install pm2 -g

sudo apt-get install nginx -y

# remove the old file and add our one
sudo rm /etc/nginx/sites-available/default
sudo cp /home/ubuntu/app_env/nginx.default /etc/nginx/sites-available/default

# finally, restart the nginx service so the new config takes hold
sudo service nginx restart

# kill npm process
killall npm
killall nodejs

export DB_HOST=mongod://10.0.1.13:27017/posts

sudo npm install /home/ubuntu/app
sudo node /home/ubuntu/app/seed/seed.js

npm start --prefix /home/ubuntu/app &

# env variable - $DB_HOST
# npm install
# nodejs seed.js
# npm start
# 
