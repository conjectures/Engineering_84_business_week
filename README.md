# Vagrant
```bash
# Automatically create a vagrant file with <image> as os
vagrant init <image>
# Spin up the virtual machine based on the Vagrantfile
vagrant up
vagrant destroy
vagrant reload
vagrant 
```
![Vagrant Process Cycle](vagrant.png)
# Linux commands:
```bash
# name of pc
uname

# list directories
ls

# make directory
mkdir <name>

# create file
touch <file name>

# escalate priviliges (admin)
sudo <command>

# change user to root
sudo su

# go up one directory
cd ..

# Print working directory
pwd

# Rename, or move files
mv <old-filename> <new-filename>

# Copy file
cp <filename> <path>

# Delete file
rm <filename>

# List files with more info (and permissions)
```

- attach box to ip in private network

We can install a webserver to check that the network works
```
sudo apt install nginx -y
```
Check status of process

- run tests on host machine with bundle (ruby)
rake spec

- install dependencies to pass tests
- write down install commands in a script `provision.sh`

- add shell script to the vagrantfile
- execute script with the `config.vm.provision` var

## Environment Variables
To list environment variables, we can use the `env` command:
```bash
# example shell
user@host: ~$ env
# PATH=/home/vagrant/bin:/home/vagrant/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
# LC_IDENTIFICATION=en_GB.UTF-8
# PWD=/home/vagrant
# LANG=en_US.UTF-8
# ...
```
We can also print a single environment variable with the `printenv` command
```bash
user@host: ~$ printenv PATH
# PATH=/home/vagrant/bin:/home/vagrant/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
By using printenv, we don't need to specify to bash that we are looking for variables. However, if we wanted to use `echo` we would have to add `$` before the variable name:
```bash
user@host: ~$ echo PATH

user@host: ~$ echo $PATH
# PATH=/home/vagrant/bin:/home/vagrant/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```
We can create a new variable with the use of the `export` keyword. We assign values in variables with the 'key=value' syntax
```bash
user@host: ~$ export NEW_VAR="Hello World"
user@host: ~$ echo $NEW_VAR
# Hello World
```
However, by exporting directly to the environment, the variables will only be available for the current session. If the machine shuts down or reboots, it will lose the variable we assigned.
To have the environment variable persist, we can add the export command inside the `.bashrc` or `.profile` file.
We can do that with the below 'one-liner':
```bash
user@host: ~$ echo "export MY_VAR='Hello World' >> .profile
```
The `.profile` file will get loaded on the next time we login to our system, or we can source it manually:
```bash
user@host: ~$ source .profile
```
Alternatively, the echo command can be 'piped' into the `.bashrc` file.
