
Vagrant.configure("2") do |config|

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


