Vagrant.configure("2") do |config|


# Creating third VM called controller
  config.vm.define "provisioner" do |provisioner|
    provisioner.vm.box = "generic/ubuntu1804"
    provisioner.vm.hostname = 'provisioner'
    provisioner.vm.network "private_network", ip: "192.168.33.10"
    provisioner.vm.synced_folder "provision", "/home/vagrant/provision"
    provisioner.vm.provision "shell", path: "project/entrypoint.sh"

    # config.hostsupdater.aliases = ["development.controller"]
   end

end
