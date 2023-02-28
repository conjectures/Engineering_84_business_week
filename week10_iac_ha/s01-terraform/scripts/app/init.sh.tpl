#!/bin/bash

cd /home/ubuntu/app
sudo npm install
sudo pm2 start app.js

