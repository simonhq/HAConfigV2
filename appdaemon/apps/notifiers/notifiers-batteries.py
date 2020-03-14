
# The aim of this is to do send messages about things in the house

# phone batteries
# device batteries

#supported
# #- smoke detectors
# - sensor.back_hall_nest_protect_battery_health
# - sensor.hallway_nest_protect_battery_health
# #- smartthings multisensors
# - sensor.back_door_state_battery
# - sensor.front_door_state_battery
# - sensor.dishwasher_multipurpose_sensor_battery            
# #- smartthings motion sensors
# - sensor.bathroom_motion_battery
# - sensor.toilet_motion_battery      
# #- smartthings water leak sensors
# - sensor.bathroom_water_leak_sensor_battery
# - sensor.dishwasher_water_leak_sensor_battery
# - sensor.ensuite_water_leak_sensor_battery
# - sensor.kitchen_water_leak_sensor_battery
# - sensor.laundry_water_leak_sensor_battery
# #- smartthings buttons
# - sensor.megs_button_battery
# #- Hue - coded - see below
# - sensor.ensuite_motion_sensor_battery_level
# - sensor.laundry_motion_sensor_battery_level
# - sensor.garage_motion_sensor_battery_level
# - sensor.living_room_hue_remote_battery_level
# - sensor.bedroom_hue_remote_battery_level
# - sensor.bedroom_2_hue_remote_battery_level


import appdaemon.plugins.hass.hassapi as hass
import time
import globals

class Battery_Messages(hass.Hass):
    
    mess = ""
    flag = 0
    batt = "'s phone is low on battery"
    dbatt = " device is low on battery"

    def initialize(self):
        
        # bring in the messaging module
        self.notifier = self.get_app('messaging')

        #smoke detectors
        self.listen_state(self.dbatt_set, "sensor.back_hall_nest_protect_battery_health")
        self.listen_state(self.dbatt_set, "sensor.hallway_nest_protect_battery_health")

        #door sensors
        self.listen_state(self.dbatt_set, "sensor.back_door_state_battery")
        self.listen_state(self.dbatt_set, "sensor.front_door_state_battery")

        #dishwasher
        self.listen_state(self.dbatt_set, "sensor.dishwasher_multipurpose_sensor_battery")

        #motion sensors
        #smartthings
        self.listen_state(self.dbatt_set, "sensor.bathroom_motion_battery")
        self.listen_state(self.dbatt_set, "sensor.toilet_motion_battery")
        #hue   
        self.listen_state(self.dbatt_set, "sensor.ensuite_motion_sensor_battery_level")
        self.listen_state(self.dbatt_set, "sensor.laundry_motion_sensor_battery_level")
        self.listen_state(self.dbatt_set, "sensor.garage_motion_sensor_battery_level")

        #leak sensors
        self.listen_state(self.dbatt_set, "sensor.bathroom_water_leak_sensor_battery")
        self.listen_state(self.dbatt_set, "sensor.dishwasher_water_leak_sensor_battery")
        self.listen_state(self.dbatt_set, "sensor.ensuite_water_leak_sensor_battery")
        self.listen_state(self.dbatt_set, "sensor.kitchen_water_leak_sensor_battery")
        self.listen_state(self.dbatt_set, "sensor.laundry_water_leak_sensor_battery")

        #remotes & buttons
        self.listen_state(self.dbatt_set, "sensor.living_room_hue_remote_battery_level")
        self.listen_state(self.dbatt_set, "sensor.bedroom_hue_remote_battery_level")
        self.listen_state(self.dbatt_set, "sensor.bedroom_2_hue_remote_battery_level")
        self.listen_state(self.dbatt_set, "sensor.megs_button_battery")

        #phones
        self.listen_state(self.batt_set, "binary_sensor.simon_batt_low")
        self.listen_state(self.batt_set, "binary_sensor.megan_batt_low")
        self.listen_state(self.batt_set, "binary_sensor.staci_batt_low")
        self.listen_state(self.batt_set, "binary_sensor.delia_batt_low")
        self.listen_state(self.batt_set, "binary_sensor.megan_ipad_batt_low")

        #messaging
        self.listen_state(self.batt_notify, "input_boolean.batt_notify_system")
        self.listen_state(self.dbatt_notify, "input_boolean.dbatt_notify_system")


    def batt_set(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.turn_on("input_boolean.batt_notify_system")
    
    def dbatt_set(self, entity, attribute, old, new, kwargs):
        if entity == 'sensor.back_hall_nest_protect_battery_health':
            if new != 'Ok':
                self.turn_on("input_boolean.dbatt_notify_system")
        elif entity == 'hallway_nest_protect_battery_health':
            if new != 'Ok':
                self.turn_on("input_boolean.dbatt_notify_system")
        else:
            if int(new) <= self.get_state("input_number.dbatt_alert"):
                self.turn_on("input_boolean.dbatt_notify_system")

    def dbatt_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.mess = "A battery is running low, check the battery page."
            self.turn_off("input_boolean.dbatt_notify_system")   
            self.notifier.notify(self.mess)

    def batt_notify(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.mess = ""
            self.flag = 0

            if self.get_state("binary_sensor.simon_batt_low") == "on":
                self.mess = "Simon"
                self.flag = 1

            if self.get_state("binary_sensor.megan_batt_low") == "on":
                if self.flag > 0:
                    self.mess += " & Megan"
                else:
                    self.mess = "Megan"
                    self.flag = 1
            
            if self.get_state("binary_sensor.megan_ipad_batt_low") == "on":
                if self.flag > 0:
                    self.mess += " & Megan's iPad"
                else:
                    self.mess = "Megan's iPad"
                    self.flag = 1

            if self.get_state("binary_sensor.staci_batt_low") == "on":
                if self.flag > 0:
                    self.mess += " & Staci"
                else:
                    self.mess = "Staci"
                    self.flag = 1

            if self.get_state("binary_sensor.delia_batt_low") == "on":
                if self.flag > 0:
                    self.mess += " & Delia"
                else:
                    self.mess = "Delia"
                    self.flag = 1

            self.mess += self.batt
            self.turn_off("input_boolean.batt_notify_system")   
            self.notifier.notify(self.mess)         




