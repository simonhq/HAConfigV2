# Garage Door

### This package watches the state of the Garage Door (Myq)

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* Binary Sensor - [Binary Sensor](https://www.home-assistant.io/components/binary_sensor.template/)

* Input Boolean - [Input Boolean](https://www.home-assistant.io/components/input_boolean/)

* Input Number - [Input_Number](https://www.home-assistant.io/components/input_number/)

* Sensor - 

<h4 align="left">Package Automations:</h4>

* Automation (appdaemon) to notify about low battery levels

<hr --- </hr>


This is what I do:

Logged in to SSH via Community SSH & Web Terminal add-on. (protection mode off)
Executed command:
docker exec -it homeassistant vi /usr/local/lib/python3.8/site-packages/pymyq/api.py
Changed to DEFAULT_USER_AGENT = "pymq"
Restarted HA.
Make sure to check the commands for how to use vi.

- haven't tried

You can use the docker command to switch to the container that contains the source. Here's how:
ssh to HA then run:

docker exec -t -i homeassistant /bin/bash                                                      
cd /usr/local/lib/python3.8/site-packages/pymyq                                                                
vi api.py
        change DEFAULT_USER_AGENT = "okhttp/3.10.0" to "pymq"
restart HA

