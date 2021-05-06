Vagrant.configure("2") do |config|

# Creating third VM called controller
  config.vm.define "provisioner" do |provisioner|
    provisioner.vm.box = "generic/ubuntu1804"
    provisioner.vm.hostname = 'provisioner'
    provisioner.vm.network "private_network", ip: "192.168.33.10"
    provisioner.vm.synced_folder "provision", "/home/vagrant/provision"
    provisioner.vm.synced_folder "application", "/home/vagrant/application"
    provisioner.vm.synced_folder "controller", "/home/vagrant/controller"
    provisioner.vm.provision "shell", path: "provision/entrypoint.sh"
    provisioner.ssh.forward_agent = true

    # config.hostsupdater.aliases = ["development.controller"]
   end

end
