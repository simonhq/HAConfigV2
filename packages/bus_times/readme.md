# Bus Times

### This package enables watching various bus stops and routes

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me & Renemarc

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

Sensor - [System Monitor](https://www.home-assistant.io/components/sensor.systemmonitor/)

GTFS - [GTFS](https://github.com/renemarc/home-assistant-config/tree/master/gtfs) 

<h4 align="left">Package GTFS Setup:</h4>

This has been prepared using Renemarc guide (https://github.com/renemarc/home-assistant-config/tree/master/gtfs)

* Download the new GTFS.zip file from the TransitFeeds Website (https://transitfeeds.com/p/action-buses/3)
* Rename the new file (action.zip)
* Copy the new zip file into the GTFS folder in the configuration directory
* Restart Home Assistant, and while restarting delete the current sqlite file (action.sqlite)
* Home Assistant will error, but it should create a new sqlite file with all the stops etc.
* Use sqlite3.exe to >
    * .open action.sqlite 
    * .clone action1.sqlite
    * .open action1.sqlite
    * Remove unneeded stops
        * DELETE FROM stop_times where stop_id not in (13,1803,1804,1807,1808,2916,2705,2706,2709,2710,2814,1723,3419,3418, 3406,3409,3401,4530,4529,4910,4819,4803,4804,2265,2264,1734,2534,2535,1078,1077,1300, 1299,1076,1075,1007,1008,1841,1840,1487,1486,4972,4979);
        * DELETE FROM stops where stop_id not in (13,1803,1804,1807,1808,2916,2705,2706,2709,2710,2814,1723,3419,3418,3406,3409,3401,4530,4529,4910,4819,4803,4804,2265,2264,1734,2534,2535,1078,1077,1300, 1299,1076,1075,1007,1008,1841,1840,1487,1486,4972,4979);
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

<h4 align="left">Package Automations:</h4>

Nothing yet

<hr --- </hr>