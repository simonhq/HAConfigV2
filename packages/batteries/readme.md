# Batteries

### This package watches the state of the batteries in devices and phones

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* [Binary Sensor](https://www.home-assistant.io/components/binary_sensor.template/)
* [Input_Boolean](https://www.home-assistant.io/components/input_boolean/)
* [Input_Number](https://www.home-assistant.io/components/input_number/)
* [Sensor](https://www.home-assistant.io/components/sensor/)

Additional Components

* Hue Developers Portal - [Hue Developers](https://developers.meethue.com/develop/get-started-2/)

<p> To get the state of hue motion sensors and remotes you need to setup an API key on your Hue bridge
and then using that key goto https://yourhuebridgeIP/debug/clip.html
</p>
<p>
The URL: /api/#API-KEY#/sensors - GET will then show you the sensors attached to the bridge that you can access.
</p>

<hr --- </hr>

### Phone & Device Battery notifications

The system is setup to get the battery information of peoples phones through the HA Android app and devices through integrations and Hue rest sensors. 
A sensor is used to 'convert' the phone battery level to the 'person' battery level for notifications.
An input number/input boolean is used to trigger messages via appdaemon.


<h4 align="left">Package Automations:</h4>

* Automation (appdaemon) to notify about low battery levels - in the <i>notifiers-batteries</i> app

<h4 align="left">Package Yaml includes</h4>

* Setup for Battery Entities
* Input Booleans/Input Numbers for triggering notifications on low battery levels
* Binary Sensors for the Phone Batteries (update these on new phones/app integrations)

<hr --- </hr>