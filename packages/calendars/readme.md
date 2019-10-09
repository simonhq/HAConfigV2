# Calendars

### This package connects to the google calendar and watches for events

<hr --- </hr> 

<h4 align="left">Package Credits:</h4>

Me

<hr --- </hr>

<h4 align="left">Package Dependencies:</h4>

Standard Home Assistant Components

* Sensor - 

<h4 align="left">Package Automations:</h4>

* Automation (appdaemon) to notify about upcoming events

<hr --- </hr>


node-red-node-google is not working at all 35. However, there is node-red-contrib-google node which is wrapping Google API and is working like a charm. It's also much more flexible.

Put inject node and send

{
    "calendarId": "yourIdHere@gmail.com",
    "timeMin": "2018-11-19T09:11:13.562Z",
    "timeMax": "2018-11-21T09:11:13.562Z"
}
to google node. On google node set API to calendar:v3 and Operation to events.list (of course you could leave that empty and provide everything by input node). timeMin and timeMax is what you want to create time window. Just checked it, works perfectly.

Of course, you need to configure google node but that is extremely simply (not like node-red-node-google):

generate JSON key 58
go to IAM & admin 54
create Project > editor and copy created e-mail address of created service
share your calendar with that e-mail

Within the 'Scopes' field put the following:

https://www.googleapis.com/auth/calendar
https://www.googleapis.com/auth/calendar.events
https://www.googleapis.com/auth/calendar.events.readonly
https://www.googleapis.com/auth/calendar.readonly
https://www.googleapis.com/auth/calendar.settings.readonly
Having all of those might be overkill for your use but that is all the Scopes for the Calendar API



This very easy to do using Node Red and an Http Request Node if any one needs it .
Just use http request node with this url: http://your.hassio.ip.address:your_hassio_port_#/api/states/your.entity_id
and get a long lived token from frontend and set token type to bearer and http type to post.
Then pass the desired state to the http node with any other node you want like inject or change node with msg.payload reflecting the state desired in json format.