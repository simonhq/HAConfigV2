#
# This sends information notifications when triggered by home assistant
#
#


import appdaemon.plugins.hass.hassapi as hass
from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta
import globals

class CalNotifier(hass.Hass):

    # message offsets in days for each event - can move these to the apps.yaml...
    daylead = 1     #(bin, recycling, greenwaste, skip, cleaner, )
    weeklead = 8    #(dandd)

    basemessage = ""
    dtitle = ""

    def initialize(self):

        # bring in the messaging module
        self.notifier = self.get_app('messaging')
        
        #messaging
        self.listen_state(self.messages, "input_boolean.send_message", new = "on")


    def messages(self, entity, attribute, old, new, kwargs):
        
        rightnow = datetime.now().hour    #get the hour that this is being called at
        onedaylead = datetime.now() + timedelta(days=self.daylead) #get the lead time date for tomorrow
        oneweeklead = datetime.now() + timedelta(days=self.weeklead) #get the lead time date for next week
        tosend = 0
        #self.log(str(self.onedaylead.date()) + " " + str(self.oneweeklead.date()))

        # run messages in the morning and evening, different information
        if rightnow < 12: #morning

            # check and send d&d message if morning with one week lead time
            vdnd = self.get_state("input_datetime.cal_dnd")
            if str(vdnd) == str(oneweeklead.date()):
                self.dtitle = "Session " + str(self.get_state(vdnd))
                self.log("dandd message")
                self.notifier.notify(self.dtitle, True)

            #set the morning message
            self.basemessage = "Good Morning, "

            # build the emoticons for rain
            if float(self.get_state("sensor.dark_sky_precip_probability_0d")) >= 70.0:
                self.basemessage += ":umbrella:" 
            elif float(self.get_state("sensor.dark_sky_precip_probability_0d")) < 70.0 and float(self.get_state("sensor.dark_sky_precip_probability_0d")) >= 50.0:
                self.basemessage += ":closed_umbrella:"

            # who is cooking
            self.basemessage += "\n\nCooking Tonight: " + self.get_state("input_select.cooking") + "\n\n"  

            # standard calendar info for today
            if self.get_state("binary_sensor.cal_cln_on") == "on":
                self.basemessage += "Tony is coming to clean today, ensure everything is tidy, please!" + "\n"
            if self.get_state("binary_sensor.cal_bin_on") == "on":
                self.basemessage += "Has the bin been put out?" + "\n"
            if self.get_state("binary_sensor.cal_rec_on") == "on":
                self.basemessage += "Has the recycling been put out?" + "\n"
            if self.get_state("binary_sensor.cal_grw_on") == "on":
                self.basemessage += "Has the green waste been put out?" + "\n"
            if self.get_state("binary_sensor.cal_skp_on") == "on":
                self.basemessage += "Anything extra for the skip?" + "\n"

            # weather for today
            self.basemessage += "\nWeather today: \n"
            self.basemessage += "Min/Max: " + self.get_state("sensor.dark_sky_overnight_low_temperature_0d") + "/" + self.get_state("sensor.dark_sky_daytime_high_temperature_0d") + "\n"
            self.basemessage += "Chance of Rain: " + self.get_state("sensor.dark_sky_precip_probability_0d") + "\n"
            self.basemessage += "Windspeed: " + self.get_state("sensor.dark_sky_wind_speed_0d") + "\n"
            self.basemessage += "UV Index: " + self.get_state("sensor.dark_sky_uv_index_0d") + "\n"
            self.basemessage += "\nHave a great day"
            #always send in the morning
            tosend = 1

        else:   #evening

            #get the things to check for tomorrow
            #vcln = self.get_state("input_datetime.cal_cln")
            vcln = self.get_state("calendar.cleaner", attribute="start_time")
            #vbin = self.get_state("input_datetime.cal_bin")
            vbin = self.get_state("calendar.bin", attribute="start_time")
            #vrec = self.get_state("input_datetime.cal_rec")
            vrec = self.get_state("calendar.recycling", attribute="start_time")
            #vgrw = self.get_state("input_datetime.cal_grw")
            vgrw = self.get_state("calendar.greenwaste", attribute="start_time")
            #vskp = self.get_state("input_datetime.cal_skp")
            vskp = self.get_state("calendar.skipbin", attribute="start_time")

            vsblanket = self.get_state("binary_sensor.sbed")
            vmblanket = self.get_state("binary_sensor.mbed")
            vstblanket = self.get_state("binary_sensor.stbed")
            vdblanket = self.get_state("binary_sensor.dbed")

            #set the evening message
            self.basemessage = "Good Evening, \n\n"
                            
            if self.get_state("binary_sensor.cal_dnd_on") == "on":
                self.basemessage += "Have fun at D&D guys!" + "\n"
                tosend = 1
                
            #self.log(str(vcln)[0:11]+" "+str(onedaylead)[0:11])
            #if str(vcln) == str(onedaylead.date()):
            if str(vcln)[0:11] == str(onedaylead)[0:11]:
                self.basemessage += "Tony is coming to clean tomorrow." + "\n"
                tosend = 1

            #if str(vbin) == str(onedaylead.date()):
            if str(vbin)[0:11] == str(onedaylead)[0:11]:
                self.basemessage += "Bin pick up is tomorrow morning, put it out, please." + "\n"
                tosend = 1

            #if str(vrec) == str(onedaylead.date()):
            if str(vrec)[0:11] == str(onedaylead)[0:11]:
                self.basemessage += "Recycling pick up is tomorrow morning, put it out, please." + "\n"
                tosend = 1

            #if str(vgrw) == str(onedaylead.date()):
            if str(vgrw)[0:11] == str(onedaylead)[0:11]:
                self.basemessage += "Green waste pick up is tomorrow morning, put it out, please." + "\n"
                tosend = 1

            #if str(vskp) == str(onedaylead.date()):
            if str(vskp)[0:11] == str(onedaylead)[0:11]:
                self.basemessage += "Skip Bin pick up is tomorrow, go fill it up, please." + "\n"
                tosend = 1
# blankets
            if vsblanket == 'on':
                self.basemessage += "Simon's electric blanket will turn on tonight." + "\n"
                tosend = 1

            if vmblanket == 'on':
                self.basemessage += "Megan's electric blanket will turn on tonight." + "\n"
                tosend = 1

            if vstblanket == 'on':
                self.basemessage += "Staci's electric blanket will turn on tonight." + "\n"
                tosend = 1

            if vdblanket == 'on':
                self.basemessage += "Delia's electric blanket will turn on tonight." + "\n"
                tosend = 1
# finish message
            #sign off
            self.basemessage += "\nHave a lovely night!"

        # only send if something to say (always will send morning, sometimes in the evening)
        if tosend > 0:
            self.log(self.basemessage)
            self.notifier.notify(self.basemessage)

        #set the check flag back off after sending messages
        self.turn_off("input_boolean.send_message")

            