# Rushbrook Overlook Configuration v2

## Installation

So I followed kiwijunglist [Post](https://community.home-assistant.io/t/this-is-how-i-installed-hass-io-on-ubuntu-with-docker-portainer-via-ssh/71743) on the forum 
on how to install hassio in a docker container, here are the steps;

* Install Ubuntu or Xubuntu

* Open a terminal and gain root access

```
    $ sudo -s
```

* Upgrade and Update all software on the machine

```
    $ apt-get upgrade

    $ apt-get update
```

* Ensure the prequistes are installed

```
    $ apt-get install -y bash jq curl avahi-daemon dbus network-manager apparmor-utils

    $ apt-get install -y apt-transport-https ca-certificates curl software-properties-common
```

* Download Docker repository and check fingerprint

```
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```
    $ add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

* Install Docker 

```
    $ apt-get update

    $ apt-get install docker-ce
```

* Install Hassio

```
    $ curl -sL https://raw.githubusercontent.com/home-assistant/hassio-build/master/install/hassio_install | bash -s
```

* Install Portainer

```
    $ docker pull portainer/portainer

    $ docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```

* Check Portainer

```
    $ docker ps
```

* Check IP information for the computer

```
    $ ifconfig
```

* Web interfaces will now be available:

Hassio - http://xxx.xxx.xxx.xxx:8123
Portainter - http://xxx.xxx.xxx.xxx:9000

to install a particular version of Hassio

ssh in to the command line

> hassio ha update --version=0.96.4


## Delete duplicate entities:

Delete entities in /config/.storage/core.entity_registry

## Slow boot times

Delete cast entities in /config/.storage/core.entity_registry
Delete cast entities in /config/.storage/core.device_registry
comment the discovery, zeroconf and ssdp config entries
restart and then uncomment the config entries

## Wireguard

```
sudo add-apt-repository ppa:wireguard/wireguard
sudo apt-get update
sudo apt-get install wireguard
```

## Pi-hole

```
sudo netstat -tulpn | grep ":53"
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved.service
```

## Plex

Discover drive

lsblk
df -T

Mount Drive

mkdir -p /usr/share/media-drive
sudo mount /dev/sdb1 /usr/share/media-drive

for permanent
echo "# Secondary Hard Drive" >> /etc/fstab
echo "/dev/sdb1 /usr/share/media-drive ntfs defaults,noatime 0 2" >> /etc/fstab
