#! /bin/bash

# Update the sources list
sudo apt-get update -y

sudo apt-get upgrade -y
# install git
#sudo apt-get install git -y

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

# source environment variables
#eval "$(./env_vars.sh)"
# no login
echo "export DB_HOST=mongodb://10.0.1.13:27017/posts" >> /home/ubuntu/.bashrc
. $HOME/.bashrc
# with login
echo "export DB_HOST=mongodb://10.0.1.13:27017/posts" >> /home/ubuntu/.profile
. $HOME/.profile

chmod +x /home/ubuntu/app/app.js

cd /home/ubuntu/app/

sudo npm install 
sudo node /app/seed/seed.js

npm install --production
npm prune --production
echo -e "\nApp deployed!\n\n"
npm start &

# 
# npm start --prefix /home/ubuntu/app &

# env variable - $DB_HOST
# npm install
# nodejs seed.js
# npm start
# 
