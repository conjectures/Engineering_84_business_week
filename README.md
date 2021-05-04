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


## Task
We will create three Virtual Machines with Vagran that correspond; the *Controller*, the *Web* and the *Database* servers.
The configuration of the machines can be seen in the `Vagrant` file.
The aforementioned machines, aliased as `controller`, `web` and `db` have been assigned with IPs `192.168.33.12`, `192.168.33.10` and `192.168.33.11` accordingly.

After spinning up the machines, we can `ssh` from the *Controller* with password `vagrant`
After installing the provision file inside the controller, we can check if ansible was installed correctly
We can use `ansible --version`

In the `/etc/ansible/hosts`, we need to add the connections
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
