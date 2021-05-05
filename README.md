# Ansible

Ansible is a popular IT automation engine that automates configuration management, cloud provisioning, software deployment and service orchestration.
## Benefits
### Simple
It uses `yaml`,
### Agentless
That is, when you create a controller, it contains the Ansible controller, but it does not require any configuration tool installation on the nodes it controls.
### Secure
It uses `ssh` to connect to other servers.
### Efficient SDLC
Integrates with other tools, 
We can change provider very easily.

## Architecture

In this example, we will create three Virtual Machines with Vagran that correspond; the *Controller*, the *Web* and the *Database* servers.
The configuration of the machines can be seen in the `Vagrant` file.

![architecture](architecture.png)

## Task
The aforementioned machines, aliased as `controller`, `web` and `db` have been assigned with IPs `192.168.33.12`, `192.168.33.10` and `192.168.33.11` accordingly.

After spinning up the machines, we can `ssh` from the *Controller* with password `vagrant`

We need to install `ansible` on the controller, so we create a shell script that includes the commands needed to install it.
The shell script, called `provision.sh` can be found on the repository.
After installing the provision file in the controller virtual machine, we can check if ansible was installed correctly
We can use `ansible --version`

In the `/etc/ansible/hosts`, we can add the connection configurations, like hostnames, passwords, etc.
```
[web]
192.168.33.10 ansible_connection=ssh ansible_ssh_user=vagrant ansible_ssh_pass=vagrant
```

We can check if ansible has a connection with the server with the `ping` module:
```bash
ansible -m ping web
```
If the `ping` works, we would receive a message back like the one below:
```bash
192.168.33.10 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
```

## Ad-hoc commands
When we bring up the machines with vagrant, or any other cloud provider, we can 'send' some commands to the servers that are connected 

We can run thses commands with the `-a` flag, which is used to pass module arguments.
For example, we can run:
```bash
ansible web -m shell -a 'ls -a'
```

We can run the commands to all the agent servers if we use `all` instead of a specific server.
For example, the below command will ping all the agent servers connected to the controller
```bash
ansible all -m ping
```

## Tasks
- Task 1: Find the `uptime` of the `db` server using ansible *ad-hoc* commands

  Once we make sure that the `db` server is connected to the controller (is entered in the `/etc/ansible/hosts` file) we can use `uptime` with the below `ad-hoc` command:
  ```bash
  ansible db -m shell -a 'uptime'

  ```
- Task 2: Update and upgrade all packages in all agents using *ad-hoc* commands:

  We can update and upgrade using the `shell` module again:
  ```bash
  ansible all -m shell -a 'sudo apt-get update -y && sudo apt-get upgrade -y'
  ```
