# Vagrant Task: Multi Machine Setup
> Time: 120 - 180'

## Summary
The sample application has the ability to connect to a database. 
We need to provision our development environment with a Virtual Machine for the database and one for the Database.

Vagrant is capable of running two or more virtual machines at once with different configurations.

## Tasks
- Research how to create a multi-machine Vagrant environment.
- Add a second virtual machine called "db" to your Vagrant file
- Configure the db machine with a different IP from the app
- Provision the db machine with a MongoDB database

## Notes
When you have the second machine running, further configuration of the app is required to make use of the database. 
We will cover this in the next lesson.

You can test if your database is working correctly by running the test suite in the test folder. 
There are two sets of tests. One for the app VM and one for the db VM. Make them all pass.

```bash
# Test the app
cd test
rake spec
```
## Acceptance Criteria
- Uses vagrant file
- Create 2 VM APP and Mongod
- Localhost set to development.local
- App works on Port 3000 (development.local:3000)
- Work with only command "vagrant up" &/or mininum commands

- If all tests succeed, it should work on the url `/posts` as well as `/fibonacci/30` 
- Additionally, documentation should exist in the README.md file.
  Documentation includes: Intro (purpose of repo), Pre Requisits and Intructions
  Instructions have a clear step by step. 
- Repo exists on github


## Documentation
Dependencies:
- Vagrant (and virtualiser)
- Ruby
- Git

To run this example, git clone main repo, then run `vagrant up`. 

## Solution

### Vagrantfile
To enable multi-machine Vagrant deployment, we need to create two different boxes in the Vagrantfile.
We can do that with the use of the `config.vm.define` variable. We can then name the variable that will associate with the specific box.
For example in the `Vagrantfile` we define two different boxes, the `db` and `app`. Each of the boxes holds a virtual machine and hosts funcitonality related to their name.
```ruby

  config.vm.define "db" do |db|
    db.vm.box = "generic/ubuntu1604"
    db.vm.network "private_network", ip:"192.168.10.101"
    db.vm.synced_folder "db", "/home/vagrant/db"
    db.vm.provision "shell", path: "db/environment/entrypoint.sh"
  end

  config.vm.define "app" do |app|
    app.vm.box = "generic/ubuntu1604"
    app.vm.network "private_network", ip:"192.168.10.100"
    app.vm.synced_folder "app", "/home/vagrant/app"
    app.vm.provision "shell", path: "app/environment/provision.sh"
  end

end
```

For each box, we need to define an operating system image, in this case, we create both boxes with **ubuntu 16.04 xenial**.
We assign a static ip in out private network for each box with the `config.vm.network` variable. To work on each of the boxes, we replace the `config` keyword with the relevant box name.

Additionally, we need to transfer files to each of the boxes in order to have a working app. To do this we use **synced folders** between our host machine and the guests, with the help of vagrant. 
This can be achieved with the `config.vm.synced_folder` keyword, then specify the name of the folder we want to sync, as well as the 'mount point' on the virtual box.

With this addition, we can not only have project files on the boxes, but we can sneak some configuration files too. In each of the virtual machines, we include a folder named `environment` that contains a shell script that has initialisation commands.

### Hostfile
As we would like to use a url in the browser, instead of inserting an ip, we have added an 'alias' for the application's ip to the `/etc/hosts` file.
The `/etc/hosts`  file acts as the first line DNS resolver on our own system, therefore we can use it to add a url for our app during development. 
We added the following line:
```bash
# In /etc/hosts
192.168.10.100    development.local
```
The above change can be performed automatically with a vagrant plugin, `vagrant-hostupdater` that can be added directly in the Vagrantfile.

### Entrypoint - App

The initialisation script for application VM is named `provision.sh` in this shell we have the following commands:
```bash
#!/bin/bash
# Update and upgrade system
sudo apt update -y && sudo apt upgrade -y
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
```
Firstly we update our packages to have everything up to date, that is available. After that, we install nginx.
Nginx gets enabled and appears on `port80` automatically when installed.
After that we install a specific version of nodejs with its dependencies. Additionally, we install `pm2` globally with `npm` - `npm` gets installed along with nodejs.

After all the packages for node are installed, we need to install the project dependencies. For that we run `npm install` in the folder with the project files.
Finally, we export the variable `DB_HOST` that tells the app where to find the database and we launch it with `npm start`

### Entrypoint - Databse
For the database, we have chosen to use a specific version of **MongoDB**. The initialisation commands for mongodb v3.2.20 are shown below:
```bash
# In entrypoint.sh
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
```
Firstly, we add a key to the aptitude manager, so that we can tell it it's safe to look in that repository.
Then we add the repo to our sources list, so that aptitude knows where to look to download the package.
Then, since we want to download a specific version of mongodb, we write that after each package, so that we don't download any other version by mistake.

After mongodb gets installed, we need to set up the MongoDB environment.
This involves us creating a folder named `/data/db` so that it can store all its data and later change some permissions.

As an added requirement, we have to change the ip the database expects traffic from, from `127.0.0.1` to `0.0.0.0`.
This means that the database will accept requests from any ip, instead for waiting for traffic from inside the same machine.
We do that with the use of `sed`, a text manipulation tool, and regular expression substitution. The setting needs to be adjusted in the `/etc/mongod.conf` file.

Finally we start the database with `sudo service mongod start` and `systemctl enable mongod.service`.


### Tests
The above configurations were based on the tests that were provided in the `test` folder. To compile and run the tests, we use the `bundler` plugin for ruby.
The tests are executed with the command `rake spec` inside the test folder.

### Reverse Proxy with NGINX
Defautl location for our nginx configuration file is `/etc/nginx`
The available sites are listed under `/etc/nginx/sites-available` with the `default` available site being available at port 80.
We can add our site in the `default` nginx site.
