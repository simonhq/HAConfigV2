# Bus Travel

### This package tries to determine what bus people are on, to help decide changes and messages

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* [Zone](https://www.home-assistant.io/components/zone/) 
* [Timer](https://www.home-assistant.io/components/timer/)
* [Input Select](https://www.home-assistant.io/components/input_select/) 
* [Sensor](https://www.home-assistant.io/components/sensor/) 

<h4 align="left">Package Yaml includes</h4>

* Setup for Input Select (to trigger transitions between zones) 
* Setup for Timer (to trigger potential buses on similar routes)
* Setup for Automations (to watch leaving and entering zones to guess routes)
* See Appdaemon - notifiers-bus.py for the messaging

<hr --- </hr>