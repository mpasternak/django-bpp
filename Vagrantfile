# -*- coding: utf-8 -*-
# -*- mode: ruby -*-
# vi: set ft=ruby :

#
# Boxy są zdefiniowane tutaj: 
# 
# 	https://github.com/mpasternak/vagrant-boxes
# 
# Sugerowane pluginy:
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
      master.vm.box = "mpasternak/base-buildbox-trusty64"
      master.vm.hostname = 'bpp-master'
      master.vm.network "private_network", ip: "192.168.111.100"

      master.vm.provision "shell", inline: "provisioning/master.sh"
  end

  config.vm.define "staging" do |staging|
      staging.vm.box = "mpasternak/base-trusty64"
      staging.vm.hostname = 'bpp-staging'
      staging.vm.network "private_network", ip: "192.168.111.101"
  end

  config.vm.define "db" do |db|
      db.vm.box = "mpasternak/base-trusty64"
      db.vm.hostname = 'bpp-db'
      db.vm.network "private_network", ip: "192.168.111.102"

      db.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/provision-db.yml"
      end
  end

  config.vm.define "selenium", primary: true do |selenium|
      selenium.vm.box = "mpasternak/base-selenium-trusty64"
      selenium.vm.hostname = 'bpp-selenium'
      selenium.vm.network "private_network", ip: "192.168.111.150"
  end

end
