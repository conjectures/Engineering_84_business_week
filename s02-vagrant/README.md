# Vagrant
Vagrant is an open-source product from HashiCorp used for building and maintaining portable virtual software development environments. 
It tries to simplify the software configuration management of visualisation in order to increase development productivity.
It is written in Ruby.

Vagrant uses "Provisioners" and "Providers" as building blocks to manage the development environments.
Providers are tools like VirtualBox, Hyper-V, Docker, VMware and other virtualisation software, and are used to set up and create the virtual environments.
Provisioners are tools like Ansible, Chef and Puppet that are used to configure those environments.


![Vagrant Process Cycle](vagrant.png)

## Installation
The following installation describes the installation of Vagrant on Ubuntu with `kvm` as provider and `libvirt` used to communicate with it.

Firstly, install `KVM` for Ubuntu:
```sh
sudo apt install qemu qemu-kvm libvirt-clients libvirt-daemon-system virtinst bridge-utils
```
Enable `libvirt`
```sh
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
# Check status
systemctl status libvirtd
```

Install `vagrant` and install dependencies needed at build time with `build-dep`:
```sh
sudo apt-get build-dep vagrant ruby-libvirt
```
Also, install the dependencies needed by `vagrant-libvirt`:
```sh
sudo apt-get install qemu libvirt-bin ebtables dnsmasq-base libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev libguestfs-tools
```
Finally, install the [vagrant-libvirt](https://github.com/vagrant-libvirt/vagrant-libvirt#installation) plugin
```
vagrant plugin install vagrant-libvirt
```
> It should be noted that not all 'boxes' can be run with KVM. When searching for boxes in the [Vagrant box store](https://app.vagrantup.com/boxes/search), the user should filter by provider so that `libvirt` compatible boxes show up.

Also, when the `vagrant up` command is used, the provider might also be specified, if not inside the Vagrant file.
Alternatively, specify it as an environment variable in `.bashrc` to have it permanently used as provider
```sh
export VAGRANT_DEFAULT_PROVIDER=libvirt
```

## Creating VMs with Vagrant
Automatically create a vagrant file with <image> as os
```sh
vagrant init <image>
```
The above command will automatically create a Vagrant file that contains a lot of information commented.
A basic Vagrantfile should look as follows
```ruby
Vagrant.configure("2") do |config|
  # Specify virtual machine image
  config.vm.box = "generic/ubuntu1604"
end
```
The above snippet constitutes a basic Vagrantfile setup that will provision an Ubuntu 16.04 Virtual Machine.
Vagrant will automatically go ahead and look for a file called `Vagrantfile` in the current directory and execute any code within it. If it is not found, an error is returned.
To go ahead and create the machine, insert the above snippet in `Vagrantfile` and then run it with the subcommand `up`:
```sh
vagrant up
```
When the process completes, a virtual machine will be running on the background, as prescribed in the file.
Some other useful commands are shown below:
```sh
# Make secure connection to the VM
vagrant ssh

# Destroy all VMs
vagrant destroy

# Reload the Vagrantfile and apply changes
vagrant reload

# Pause the VM
vagrant halt

# Display help menu
vagrant help
```

## Using Vagrant VM
As mentioned above, we can 'connect' to the VM with `vagrant ssh`. When the secure shell process is established we can use some [commands](#linux-commands) to perform actions.

We also want to check if the networking between the VM and the host is working properly.
First, we attache an ip in the Vagrant private network. To do that, we modify the `Vagrantfile` as follows:
```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu1604"

  # attach private network with IP
  config.vm.network "private_network", ip:"192.168.10.100"

  # Attach folder
  config.vm.synced_folder "project", "/home/vagrant/project"

  config.vm.provision "shell", path: "project/environment/provision.sh"
end
```
With the above snippet, we create specify the IP of the VM in the private network, we also 'mount' a folder from our host system as 'synced folder', then we run a provisioning file inside the mounted folder.
This provision shell installs the `NginX` webserver, and node so that we can run a nodejs project.

> Nginx is a webserver that can be used as a reverse proxy, that is, we can redirect incoming traffic from a port to our application with the url querystring, or 'path'.

After Vagrantfile is updated, we need to halt and 'reload' the file. If issues arise when halting and reloading the file, try destroying the machine with `vagrant destroy`, and then recreating it with `vagrant up`.

We could also install the webserver manually:
```sh
sudo apt install nginx -y
```
To check if the server runs properly, we can check it's status with `systemd`:
```sh
sudo systemctl status nginx
```
Alternatively, we could check the IP on our browser to see if the default `nginx` page shows up.

The application we want to run has some tests that are checking if the environment is set up correctly. 
To run these tests, (inside the host), we go inside the  `spec-tests` directory and use `rake`. However, we first need to install `rake` for ruby with the `bundler`.
The `bundler` will automatically install all the packages in the `Gemfile` inside the environment directory

```ruby
# Install bundler
gem install bundler

# Install ruby packages (gems)
bundle install

# Perform tests
rake spec
```

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


## Syncing folders
We can sync folders with our vagrant machine with the `synced_folder` variable, as shown below:
```ruby
  config.vm.synced_folder "project", "/home/vagrant/project"
```

## Linux commands
As the VM is provisioned with a Linux OS, some basic commands are shown for reference.
```sh
# Show the name of the pc
uname
# List directories
ls
# Make directory
mkdir <name>
# Create file
touch <file name>
# Escalate priviliges (admin)
sudo <command>
# Change user to root
sudo su
# Go up one directory
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
ll
```
