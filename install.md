# Rushbrook Overlook Configuration v2

## Installation

So I followed kiwijunglist [Post](https://community.home-assistant.io/t/this-is-how-i-installed-hass-io-on-ubuntu-with-docker-portainer-via-ssh/71743) on the forum 
on how to install hassio in a docker container, here are the steps;

* Install Ubuntu or Xubuntu

I also had an issue where the wifi card wasn't turned on my laptop:
    * Open the Xubuntu menu and go to Software and Updates
    * Go to the Additional Drivers tab
    * On the Wifi Card, check on the use the proprietry drivers
    * Restart the computer

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


You then have to go into

/usr/share/hassio/homeassistant 

sudo chmod -R 777 /usr/share/hassio/homeassistant 

(and again after known_devices.yaml has been created)

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