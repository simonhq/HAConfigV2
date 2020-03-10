# Addons

### This package describes what addons I am using, including setup and automations for addons

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Obviously the awesome add-on creators for Home Assistant

[HA Community Addons](https://addons.community)
[HA Google Drive Backup Repository](https://github.com/sabeechen/hassio-google-drive-backup)
[ESPHome HA Add-Ons](https://github.com/esphome/hassio)

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* Input Boolean - [Input Boolean](https://www.home-assistant.io/components/input_boolean/)


<h4 align="left">List of Addons in Use:</h4>

Key: ^^^ High usage, ^^ Some usage, ^ low usage or experimenting

<h5 align="left">Automation</h5>

* AppDaemon 4 ^^^
Python based automation and dashboarding
* Node-Red ^^^
Visual based automation
* ESPHome ^
Flashing mini-boards

<h5 align="left">Networking</h5>

* Duck DNS ^^^
Updates the Duck DNS system with latest dynamic IP
* Nginx Proxy Manager ^^^
Handles SSL connections from Duck DNS address while allowing http connections internally
* Pi-hole ^^
Ad blocking DNS server, currently only used for WireGuard connections, need to extend current network
* WireGuard ^^
VPN into home network, works well apart from our inconsistent internet connection...

<h5 align="left">Monitoring & Administration</h5>

* Glances
Shows the state of the server that home assistant is being run on
* SSH & Web Terminal
Allows access when the front-end is unavailable
* Check Home Assistant configuration
Run before upgrading to see potential issues
* Samba Share
Allows access to the directory structure on the server for in network updates
* Visual Studio Code
Allows access through a web browser for external updates if required

<h5 align="left">Database</h5>

* InfluxDB
Long term storage of information for reporting
* MariaDB
Extended database for HA and some of the addons
* phpMyAdmin
Database admin to manage MariaDB
* Hass.io Google Drive Backup
Full snapshot backups of the HA environment to Google Drive

<h5 align="left">Capability</h5>

* Bookstack
A wiki, used to keep track of non-sensitive, non-time-dependant family information
* Grafana
Graphing tool that uses the long-term data in InfluxDB
* Grocy
A home management tool to keep track of things in the house


<h4 align="left">Package Yaml includes</h4>

* Setup for InfluxDB
* Input Booleans for triggering restarting of appdaemon and node-red
* automation for restarting appdaemon and node-red

<hr --- </hr>