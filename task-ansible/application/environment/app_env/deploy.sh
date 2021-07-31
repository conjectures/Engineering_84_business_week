#!/bin/bash

export DB_HOST=mongodb://10.0.1.13:27017/posts?authSource=admin
cd app/
npm install
node seeds/seed.js
pm2 kill
sudo pm2 start app.js --name app

