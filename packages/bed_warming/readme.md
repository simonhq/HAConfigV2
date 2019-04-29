# Bed Warming

### This package watches the overnight temperature, and if it is going to be cold it will preheat the bed (turn on switch of analog electric blanket).

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* [Input Number](https://www.home-assistant.io/components/input_number/)

* [Input Boolean](https://www.home-assistant.io/components/input_boolean/)

* [Timers](https://www.home-assistant.io/components/timer/)

Weather Tracking *move this to weather*

* [Dark Sky Sensor](https://www.home-assistant.io/components/sensor.darksky/)

Mode Tracking

* The House modes used to determine current state

<h4 align="left">Package Automations:</h4>

* Automation to turn off the switches when night, morning and day or when the timer stops
* Automation to turn on the switches when evening (if overnight temperature condition met)
* Automation to turn on the switch and set the timer for an hour

<hr --- </hr>