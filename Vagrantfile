# -*- coding: utf-8 -*-
# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# Boxy są zdefiniowane tutaj: 
# 
# 	https://github.com/mpasternak/vagrant-boxes
# 
# Wymagane pluginy:
#
#  * vagrant-hostmanager
#  * vagrant-cachier
#


Vagrant.configure(2) do |config|

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.ignore_private_ip = false
  config.hostmanager.include_offline = true

  config.vm.define "master", primary: true do |master|
      master.vm.box = "ubuntu/xenial64"
      master.vm.box_check_update = false

      master.vm.hostname = 'bpp-master'
      master.hostmanager.aliases = %w(bpp-master.localnet)

      master.vm.network "private_network", ip: "192.168.111.100"

      master.vm.provision "shell", path: "provisioning/locale.sh"
      master.vm.provision "shell", path: "provisioning/add-swap.sh"
      master.vm.provision "shell", path: "provisioning/apt-fresh.sh"
      master.vm.provision "shell", path: "provisioning/tools.sh"
      master.vm.provision "shell", path: "provisioning/python.sh"

      master.vm.provision "shell", path: "provisioning/git.sh"
      master.vm.provision "shell", path: "provisioning/build.sh"      
      master.vm.provision "shell", path: "provisioning/pip.sh"      

      master.vm.provision "shell", path: "provisioning/ubuntu-14.04.sh"
      master.vm.provision "shell", path: "provisioning/ubuntu-14.04-dev.sh"
      master.vm.provision "shell", path: "provisioning/venv.sh", privileged: false
      master.vm.provision "shell", path: "provisioning/wheels.sh", privileged: false
      master.vm.provision "shell", path: "provisioning/vars.sh", privileged: false
      master.vm.provision "shell", path: "provisioning/checkout.sh", privileged: false

      # Nginx & co
      master.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/provision.yml"
      end

      if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
        config.cache.enable :apt
        config.cache.enable :npm
	config.cache.enable :generic, {
	  "wget" => { cache_dir: "/var/cache/wget" },
	}
      end
  end

  config.vm.define "staging" do |staging|
      staging.vm.box = "ubuntu/xenial64"
      staging.vm.box_check_update = false

      staging.vm.hostname = 'bpp-staging'
      staging.hostmanager.aliases = %w(bpp-staging.localnet)
      staging.vm.network "private_network", ip: "192.168.111.101"

      staging.vm.provision "shell", path: "provisioning/locale.sh"
      staging.vm.provision "shell", path: "provisioning/add-swap.sh"
      staging.vm.provision "shell", path: "provisioning/apt-fresh.sh"
      staging.vm.provision "shell", path: "provisioning/tools.sh"
      staging.vm.provision "shell", path: "provisioning/python.sh"

      if Vagrant.has_plugin?("vagrant-reload")
            staging.vm.provision :reload
      end

      if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
        config.cache.enable :apt
      end

  end

  config.vm.define "db" do |db|
      db.vm.box = "ubuntu/xenial64"
      db.vm.box_check_update = false

      db.vm.hostname = 'bpp-db'
      db.vm.network "private_network", ip: "192.168.111.102"

      db.vm.provision "shell", path: "provisioning/locale.sh"
      db.vm.provision "shell", path: "provisioning/add-swap.sh"
      db.vm.provision "shell", path: "provisioning/apt-fresh.sh"
      db.vm.provision "shell", path: "provisioning/tools.sh"
      db.vm.provision "shell", path: "provisioning/python.sh"

      db.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/provision.yml"
      end

      # Otwórz PostgreSQL po TCP/IP dla wszystkich
      db.vm.provision "shell", path: "provisioning/postgresql-open-wide.sh"

      # Zoptymalizuj PostgreSQL dla maszyny z 1 GB RAM
      db.vm.provision "file", source: "provisioning/postgresql-optimized.conf", destination: "postgresql-optimized.conf"
      db.vm.provision "shell", inline: "sudo cat postgresql-optimized.conf >> /etc/postgresql/9.5/main/postgresql.conf"
      db.vm.provision "shell", inline: "sudo service postgresql restart"

      if Vagrant.has_plugin?("vagrant-reload")
            db.vm.provision :reload
      end

      if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
        config.cache.enable :apt
      end

  end

  config.vm.define "selenium" do |selenium|
      # Na ten moment zostaje na Firefox 43 / trusty64 / selenium 2.8 do momentu
      # przeanalizowania zmian w Selenium 3-beta
      selenium.vm.box = "mpasternak/selenium-trusty64"
      selenium.vm.hostname = 'bpp-selenium'
      selenium.vm.network "private_network", ip: "192.168.111.150"
      selenium.hostmanager.aliases = %w(selenium)

      selenium.vm.provision "shell", inline: "echo 192.168.111.1 MacOSX.localnet >> /etc/hosts"

      if Vagrant.has_plugin?("vagrant-cachier")
        config.cache.scope = :box
        config.cache.enable :apt
      end
  end

end
