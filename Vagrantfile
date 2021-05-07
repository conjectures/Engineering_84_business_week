
module MySvc
  def self.password
    begin
      system 'stty -echo'
      print 'Ansible Password: '
      ; pass = $stdin.gets.chomp; puts "\n"
    ensure
      system 'stty echo'
    end
    pass
  end
end

Vagrant.configure("2") do |config|

# Creating third VM called controller
  config.vm.define "provisioner" do |provisioner|
    provisioner.vm.box = "generic/ubuntu1804"
    provisioner.vm.hostname = 'provisioner'
    provisioner.vm.network "private_network", ip: "192.168.33.10"
    provisioner.vm.synced_folder "provision", "/home/vagrant/provision"
    provisioner.vm.synced_folder "application", "/home/vagrant/application"
    provisioner.vm.synced_folder "controller", "/home/vagrant/controller"
    provisioner.vm.provision "shell", path: "provision/provision.sh"
    provisioner.ssh.forward_agent = true
    provisioner.vm.provision :shell, :path => "provision/ansible.sh", :privileged => true, :args => [MySvc.password()]
    # provisioner.vm.provision "shell", path: "provision/connection.sh"

    # config.hostsupdater.aliases = ["development.controller"]
    #
    # Ask for password 
    # provisioner.vm.provision "ansible_local" do |ansible|
    #     ansible.limit = "all"
    #     ansible.vault_password_file = "/tmp/vault_pass"
    #     ansible.playbook = "/etc/ansible/provision_playbook.yaml"
    #     ansible.vault_password_file = "/home/vagrant/provision/vault_pass"
    #     ansible.raw_arguments = [
    #         "--tags=ec2-create,ec2-controller"
    #     ]
    #     ansible.extra_vars = { ansible_python_interpreter:"/usr/bin/python3" }
    #     end
    # provisioner.vm.provision "shell", path: "provision/connection.sh"

   end

end
