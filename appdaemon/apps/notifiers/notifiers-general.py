#
#The aim of this is to do send messages about things in the house
# cooking
# washer
# dryer
# hassio laptop
# printer
#

import appdaemon.plugins.hass.hassapi as hass
import time
#import globals

class General_Messages(hass.Hass):
    
    mess = ""
    flag = 0
    #washer = "Washing Machine stopped"
    #dryer = "Dryer stopped"
    printer = "'s printer ink is low"
    disk = "Laptop Server hard drive is almost full"
    cpu = "Laptop Server CPU is very high"
    drink = "The local pressure has decreased, drink another glass of water with a 1/8tsp of salt"
    potas = "The local pressure has increased, smash some potassium"

    def initialize(self):
        
        # bring in the messaging module
        self.notifier = self.get_app('messaging')

        self.listen_state(self.disk_set, "binary_sensor.disk_alert")
        self.listen_state(self.cpu_set, "binary_sensor.cpu_alert")

        self.listen_state(self.ink_set, "binary_sensor.ink_black_alert")
        self.listen_state(self.ink_set, "binary_sensor.ink_cyan_alert")
        self.listen_state(self.ink_set, "binary_sensor.ink_magenta_alert")
        self.listen_state(self.ink_set, "binary_sensor.ink_yellow_alert")

        self.listen_state(self.printer_notify, "input_boolean.ink_notify_system")
        self.listen_state(self.disk_notify, "binary_sensor.disk_alert")
        self.listen_state(self.cpu_notify, "binary_sensor.cpu_alert")
        
        self.listen_state(self.potas_notify, "binary_sensor.diet_press_up")
        self.listen_state(self.drink_notify, "binary_sensor.diet_press_down")

        self.listen_state(self.gps_notify, "input_boolean.button_pushed")

        #nodered
        #self.listen_state(self.washing_notify, "binary_sensor.samwash")
        #self.listen_state(self.drying_notify, "binary_sensor.samdry")

        #self.listen_state(self.cook_flag, "sensor.cook_calendar") 

        #self.listen_state(self.gps_notify, "device_tracker.sphone_net")
        #self.listen_state(self.gps_notify, "device_tracker.mphone_net")
        #self.listen_state(self.gps_notify, "device_tracker.stphone_net")
        #self.listen_state(self.gps_notify, "device_tracker.dphone_net")

        # self.listen_state(self.gps_notify, "sensor.sphone_gps_up")
        # self.listen_state(self.gps_notify, "sensor.mphone_gps_up")
        # self.listen_state(self.gps_notify, "sensor.stphone_gps_up")
        # self.listen_state(self.gps_notify, "sensor.dphone_gps_up")


    # def cook_flag(self, entity, attribute, old, new, kwargs):
    #     v = self.get_state("sensor.cook_calendar")
    #     #self.log(v)
    #     cook = v[0:2]
    #     #self.log(cook)
    #     if cook == "Si" or cook == "si":
    #         self.set_state("input_select.cooking", state="Simon")
    #     elif cook == "Me" or cook == "me":
    #         self.set_state("input_select.cooking", state="Megan")
    #     elif cook == "St" or cook == "st":
    #         self.set_state("input_select.cooking", state="Staci")
    #     elif cook == "De" or cook == "de":
    #         self.set_state("input_select.cooking", state="Delia")
    #     elif cook == "Ea" or cook == "ea":
    #         self.set_state("input_select.cooking", state="Easy")
    #     elif cook == "Go" or cook == "go":
    #         self.set_state("input_select.cooking", state="Going Out")

    def ink_set(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.turn_on("input_boolean.ink_notify_system")

    def disk_set(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.turn_on("input_boolean.disk_notify_system")

    def cpu_set(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.turn_on("input_boolean.cpu_notify_system")


    #def washing_notify(self, entity, attribute, old, new, kwargs):
    #    if new == "off":
    #        self.notifier.notify(self.washer)

    #def drying_notify(self, entity, attribute, old, new, kwargs):
    #    if new == "off":
    #        self.notifier.notify(self.dryer)

    def disk_notify(self, entity, attribute, old, new, kwargs):
        if new == "off":
            self.notifier.notify(self.disk)
            self.turn_off("input_boolean.disk_notify_system")
            
    def cpu_notify(self, entity, attribute, old, new, kwargs):
        if new == "off":
            self.notifier.notify(self.cpu)
            self.turn_off("input_boolean.cpu_notify_system")

    # you also need to change the items in diet.yaml
    def drink_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.notifier.notify(self.drink)
            mbar = self.get_state("sensor.dark_sky_pressure")
            self.set_state("input_number.last_measure", state=mbar)

    def potas_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.notifier.notify(self.potas)
            mbar = self.get_state("sensor.dark_sky_pressure")
            self.set_state("input_number.last_measure", state=mbar)

    def gps_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.turn_off("input_boolean.button_pushed")
            self.notifier.notify("gps")

    def printer_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.mess = ""
            self.flag = 0

            if self.get_state("binary_sensor.ink_black_alert") == "on":
                self.mess = "Black"
                self.flag = 1

            if self.get_state("binary_sensor.ink_cyan_alert") == "on":
                if self.flag > 0:
                    self.mess += " & Cyan"
                else:
                    self.mess = "Cyan"
                    self.flag = 1
            
            if self.get_state("binary_sensor.ink_magenta_alert") == "on":
                if self.flag > 0:
                    self.mess += " & Magenta"
                else:
                    self.mess = "Magenta"
                    self.flag = 1

            if self.get_state("binary_sensor.ink_yellow_alert") == "on":
                if self.flag > 0:
                    self.mess += " & Yellow"
                else:
                    self.mess = "Yellow"
                    self.flag = 1

            self.mess += self.printer            
            self.turn_off("input_boolean.ink_notify_system")
            self.notifier.notify(self.mess)

    

    # def gps_notify(self, entity, attribute, old, new, kwargs):
    #     self.mess = ""

    #     if entity == 'sensor.sphone_gps_up':
    #         if float(self.get_state('sensor.sphone_gps_up')) >= 2:
    #             self.mess = "Hi Simon, logging hasn't reported for a while, can you check it please."
    #     elif entity == 'sensor.mphone_gps_up':
    #         if float(self.get_state('sensor.mphone_gps_up')) >= 2:
    #             self.mess = "Hi Megan, logging hasn't reported for a while, can you check it please."
    #     elif entity == 'sensor.stphone_gps_up':
    #         if float(self.get_state('sensor.stphone_gps_up')) >= 2:
    #             self.mess = "Hi Staci, logging hasn't reported for a while, can you check it please."
    #     elif entity == 'sensor.dphone_gps_up':
    #         if float(self.get_state('sensor.dphone_gps_up')) >= 2:
    #             self.mess = "Hi Delia, logging hasn't reported for a while, can you check it please."

    #     self.notifier.notify(self.mess)   



