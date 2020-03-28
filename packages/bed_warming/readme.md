# Bed Warming

### This package controls the electric blankets, for weather and timer.

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* [Input Number](https://www.home-assistant.io/components/input_number/)
* [Input Boolean](https://www.home-assistant.io/components/input_boolean/)
* [Binary Sensor](https://www.home-assistant.io/components/binary_sensor.template/)
* [Timers](https://www.home-assistant.io/components/timer/)

### Process

<img src="https://github.com/simonhq/HAConfigV2/blob/master/images/bedwarming.png" width="750"/>

Hardware

* [TP-Link Switches](https://www.tp-link.com/au/) Switches

House_Mode Package

* The House mode used to determine current state of the house

Weather Package

* [Dark Sky Sensor](https://www.home-assistant.io/components/sensor.darksky/)

<h4 align="left">Package Automations:</h4>

Node-Red used to automate the processes described
* Buttons and Remotes -> turns on and off the timer triggers (input booleans)
* Climate -> turns on and off the actual switches
* Timers -> turns off the actual switches when the timers end
* Time Actions -> turns on and off the actual switches based upon the weather

<h4 align="left">Package Yaml includes</h4>

* Setup for Input Number (to trigger weather mode) 
* Setup for Input Boolean (to trigger timer mode)
* Setup for Binary Sensor (to allow for warning that blankets will be turned on)
* Setup for Timers (to manage timer mode)

<hr --- </hr>