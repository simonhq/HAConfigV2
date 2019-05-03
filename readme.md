# Rushbrook Overlook Configuration v2

Software: [Home Assistant](https://home-assistant.io)


#### Notes

Special note: If user gets completely locked out
 * Remove both .storage/auth and .storage/onboarding to restart the onboarding process and create a new user.

Samba Share of Hassio on Xubuntu 
 * /usr/share/hassio/homeassistant
 * User - hassio


### Why v2

Over the last 18 months I have learnt a lot about the various components and hardware using Home Assistant(Hassio) on the Raspberry Pi.
After my second SD Card crashed and another fast rebuild was done so that we weren't sitting in the dark, I realised that I needed a more stable system.
The Pi has been great but the lack of harddrive and the load we are putting on it with the different components and add-ons I think an upgrade is required.

I looked at a few different options and landed upon:
* [Hassio]() - I like this version of the software, the ability to have add-ons controlled and visible in the one system appeals to me.
* Old laptop with [Xubuntu]() with [Docker]() - considered buying a specific [NUC]() and I may do that in the future, but I had an old laptop available.

Rather than run plain Home Assistant in Docker, I prefer the ability to use the add-ons, though I may change my mind in the future.

I plan on restructuring my files, at the moment all the binary_sensors are in one file and all the sensors in another, but considering that I have lots of things
dependant upon each other, I plan on moving to a package system to keep things together.

Here is a Todo list of packages:

* Interface/Lovelace

## Packages Done (1st draft)

* Batteries
* Bed Warming
* Bus Times
* Bus Travel
* Calendars
* Car Times
* Climate
* Cooking
* Date/Time
* Devices
* Doors
* Fans
* Garage Door
* GPS
* Harmony Remote
* House Modes (Time)
* Hue Remotes
* IFTTT
* Lights
* Mode Actions (Time & Presence)
* Motion Sensors/Lights
* Notifiers
* Pi-Hole
* Presence
* Printer
* Switches
* System Monitor
* Travel Control
* Weather

## Integrations

* External IP/Duckdns
* Hue Lights
* Smartthings
* TP-Link Switches
* Nest
* IFTTT
* GPS Logger
* Google Cast
* Discord Webhook
* Appdaemon Automations 

#### Errors
* Google Hangouts

## Installation

[Installation Detail](./install.md)

## System Detail


