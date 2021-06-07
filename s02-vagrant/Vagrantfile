
Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu1604"

  # attach private network with IP
  config.vm.network "private_network", ip:"192.168.10.100"

  # Attach folder
  config.vm.synced_folder "project", "/home/vagrant/project"

  # Alias ip with vagrant-hostupdater
  # config.hostupdater.aliases = ["development.local"]

  config.vm.provision "shell", path: "project/environment/provision.sh"
end


