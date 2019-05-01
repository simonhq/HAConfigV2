# Car Times

### This package uses the waze travel time to calculate times to pick up people and get to work.

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* Binary Sensor - [Binary Sensor](https://www.home-assistant.io/components/binary_sensor.template/)

* Input Boolean - [Input Boolean](https://www.home-assistant.io/components/input_boolean/)

* Timer - [Timers](https://www.home-assistant.io/components/timer/) 

* Sensor - []()

* Waze Travel Times - [Waze Travel Time](https://www.home-assistant.io/components/sensor.waze_travel_time/)

* IFTTT - [IFTTT](https://www.home-assistant.io/components/ifttt/)
* Tasker - []() 


Other Packages

* IFTTT_hooks - to accept/process webhooks
* Travel      - guess of what modes of travel people are using

<h4 align="left">Package Automations:</h4>

* When a phone connects to the car bluetooth, Tasker sends to IFTTT which sends a webhook to HA saying that the person is driving

<hr --- </hr>