#!/bin/bash


# Add mongodb to sources
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
# Update package list
sudo apt-get update
# Install mongodb
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20

# Edit mongodb conf
sudo mkdir -p /data/db
sudo chown -R mongodb:mongodb /var/lib/mongodb
# Change loopback ip (for test)
sudo sed -i 's/127.0.0.1/0.0.0.0/g' /etc/mongod.conf

# # Start mongodb service
sudo service mongod start
sudo systemctl enable mongod.service
