
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
    provisioner.vm.network "private_network", ip: "192.168.33.11"
    provisioner.vm.synced_folder "provision", "/home/vagrant/provision"
    provisioner.vm.synced_folder "application", "/home/vagrant/application"
    provisioner.vm.synced_folder "controller", "/home/vagrant/controller"
    # provisioner.vm.provision "shell", path: "provision/provision.sh"
    provisioner.ssh.forward_agent = true
    provisioner.vm.provision :shell, :path => "provision/provision.sh", :privileged => true, :args => [MySvc.password()]

  end

end
