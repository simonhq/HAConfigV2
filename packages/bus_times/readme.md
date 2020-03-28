# Bus Times

### This package enables watching various bus stops and routes using GTFS

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me & Renemarc

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

### Standard Home Assistant Components

* [Sensor](https://www.home-assistant.io/components/sensor/)
* [GTFS](https://github.com/renemarc/home-assistant-config/tree/master/gtfs) 
* [Input Boolean](https://www.home-assistant.io/components/input_boolean/)

### Special GTFS 

If you are using [HACS](https://hacs.xyz/) and [Appdaemon](https://appdaemon.readthedocs.io/en/latest/AD_API_REFERENCE.html) then you can use
the Clean_GTFS module - available in HACS - that I have written to do the majority of the complications in having GTFS work in HA.

You will still need to do the following:

* Download the new GTFS.zip file from the [TransitFeeds](https://transitfeeds.com/) Website.
* Rename the new file to what you have setup in your Appdaemon App.
* Copy the new zip file into the GTFS folder in the configuration directory of HA.
* Delete the current sqlite file in the directory.
* Restart home assistant and wait for it to create the new sqlite file. (Errors will show in the HA log file.)
* Trigger the Clean-GTFS module.
* Restart home assistant.

### Manual GTFS

<h4 align="left">Package GTFS Setup:</h4>

This has been prepared using Renemarc guide (https://github.com/renemarc/home-assistant-config/tree/master/gtfs)

* Download the new GTFS.zip file from the [TransitFeeds](https://transitfeeds.com/) Website.
* Rename the new file (action.zip)
* Copy the new zip file into the GTFS folder in the configuration directory
* Restart Home Assistant, and while restarting delete the current sqlite file (action.sqlite)
* Home Assistant will error, but it should create a new sqlite file with all the stops etc.
* Use sqlite3.exe to >
    * .open action.sqlite 
    * .clone action1.sqlite
    * .open action1.sqlite
    * Remove unneeded stops
        * DELETE FROM stop_times where stop_id not in (xxx, xxxx, xxxx);
        * DELETE FROM stops where stop_id not in (xxx, xxxx, xxxx);
    * Create indexes
        * CREATE INDEX idx_trips_service_id ON trips(service_id);
        * CREATE INDEX idx_stop_times_stop_id ON stop_times(stop_id);
        * CREATE INDEX idx_stop_times_trip_id ON stop_times(trip_id);
        * CREATE INDEX idx_stop_times_stop_sequence ON stop_times(stop_sequence);
        * CREATE INDEX idx_stop_times_departure_time ON stop_times(departure_time);
        * UPDATE routes SET agency_id = (SELECT agency_id FROM agency);
    * vacuum;
* Restart Home Assistant, and while restarting...
* Rename action.sqlite to back_up.sqlite
* Rename action1.sqlite to action.sqlite

<h4 align="left">Package Yaml includes</h4>

* Setup for Input Boolean (to trigger Clean-GTFS)
* Setup for GTFS bus stop watches 

<hr --- </hr>