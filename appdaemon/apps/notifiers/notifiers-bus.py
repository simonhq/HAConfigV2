#
#The aim of this is to do send messages about transport
#

import appdaemon.plugins.hass.hassapi as hass
import time
#import globals

class Transport_Messages(hass.Hass):

    smess_lcw = "Simon just left City West on R5" #R5CW
    smess_anu = "Simon just left ANU on the R4" #R4CW
    smess_woden = "" #R4W
    smess_tugg_home = "Simon just left Tuggeranong travelling home" #7X
    smess_tugg = "Simon just left Tuggeranong Interchange" #TX
    smess_cal = "Simon just arrived in Calwell" #Cal

    stmess_cit = "Staci just left the city heading home" #R234
    stmess_woden = "" #R4W
    stmess_tugg_home = "Staci just left Tuggeranong travelling home" #7X
    stmess_tugg = "Staci just left Tuggeranong Interchange" #TX
    stmess_cal = "Staci just arrived in Calwell" #Cal
    stmess_ctr = "Staci just arrived at Central in Sydney" #Syd

    dmess_uc = "Delia just left UC heading to the city" #R234
    dmess_woden = "" #R4W
    dmess_tugg_home = "Delia just left Tuggeranong travelling home" #7X
    dmess_tugg = "Delia just left Tuggeranong Interchange" #TX
    dmess_cal = "Delia just arrived in Calwell" #Cal
    dmess_ctr = "Delia just arrived at Central in Sydney" #Syd

    mmess_woden = "" #R4W
    mmess_tugg_home = "Megan just left Tuggeranong travelling home" #7X
    mmess_tugg = "Megan just left Tuggeranong Interchange" #TX
    mmess_cal = "Megan just arrived in Calwell" #Cal
    mmess_car = "Megan is heading to the car from work"
    mmess_bus = "Megan is heading home via bus from work"


    def initialize(self):
        
        # bring in the messaging module
        self.notifier = self.get_app('messaging')

        self.listen_state(self.reset_transport, "input_boolean.mode_return_home")
        self.listen_state(self.transport_simon, "input_select.trans_simon")
        self.listen_state(self.transport_megan, "input_select.trans_megan")
        self.listen_state(self.transport_staci, "input_select.trans_staci")
        self.listen_state(self.transport_delia, "input_select.trans_delia")
        #set messaging platform
        #self.listen_state(self.mess_flag, "input_select.message_flag")
        #self.listen_state(self.screens, "input_select.presence_mode") # done in automation/presence

    #def mess_flag(self, entity, attribute, old, new, kwargs):
    #    self.mess_platform = self.get_state("input_select.message_flag")
    
    def screens(self, entity, attribute, old, new, kwargs):
        sflag = 0
        if new == "Someone Home" and old == "All Away":
            sflag = 1
        elif new == "All Home" and old == "All Away":
            sflag = 1
        elif new == "All Away":
            sflag = 2
        else:
            sflag = 3

        if sflag == 1:
            self.call_service(self.hnotify,message=self.hmessage_home)
        elif sflag == 2:
            self.call_service(self.hnotify,message=self.hmessage_away)

    ################## look at this

    def reset_transport(self, entity, attribute, old, new, kwargs):
        if new == "off":
            self.set_state("input_select.trans_simon", state="Nil", attributes={"options": ['Nil','R5CW','R4CW','RC','RW','R5T','R4T','7X','TX','Cal','Car'], "icon":"mdi:car-connected", "friendly_name":"Transport Simon"})
            self.set_state("input_select.trans_megan", state="Nil", attributes={"options": ['Nil','RC','RW','R5T','R4T','7X','TX','Cal','Car'], "icon":"mdi:car-connected", "friendly_name":"Transport Megan"})
            self.set_state("input_select.trans_staci", state="Nil", attributes={"options": ['Nil','RC','RW','R5T','R4T','7X','TX','Cal','Car'], "icon":"mdi:car-connected", "friendly_name":"Transport Staci"})
            self.set_state("input_select.trans_delia", state="Nil", attributes={"options": ['Nil','R234','RC','RW','R5T','R4T','7X','TX','Cal','Car'], "icon":"mdi:car-connected", "friendly_name":"Transport Delia"})

    ################## look at this      

    def transport_simon(self, entity, attribute, old, new, kwargs):
        if self.get_state("input_boolean.mode_return_home") == "on":
            if new == "R5CW":
                self.notifier.notify(self.smess_lcw)
            elif new == "R4CW":
                self.notifier.notify(self.smess_anu)
            elif new == "RW":
                self.smess_woden = "Simon at Woden, R4 to Tugg79 " + self.get_state("sensor.tugg_to_home_79_homecheck") + " or R5 " + self.get_state("sensor.woden_to_home_r5_homecheck")
                self.notifier.notify(self.smess_woden)
            elif new == "7X":
                self.notifier.notify(self.smess_tugg_home)
            elif new == "TX":
                self.notifier.notify(self.smess_tugg)
            elif new == "Cal":
                self.notifier.notify(self.smess_cal)

    def transport_delia(self, entity, attribute, old, new, kwargs):
        if self.get_state("input_boolean.mode_return_home") == "on":
            if new == "R234":
                self.notifier.notify(self.dmess_uc)
            if new == "RW":
                self.dmess_woden = "Delia at Woden, R4 to Tugg79 " + self.get_state("sensor.tugg_to_home_79_homecheck") + " or R5 " + self.get_state("sensor.woden_to_home_r5_homecheck")
                self.notifier.notify(self.dmess_woden)
            elif new == "7X":
                self.notifier.notify(self.dmess_tugg_home)
            elif new == "TX":
                self.notifier.notify(self.dmess_tugg)
            elif new == "Cal":
                self.notifier.notify(self.dmess_cal)
            elif new == "Central":
                self.notifier.notify(self.dmess_ctr)

    def transport_megan(self, entity, attribute, old, new, kwargs):
        if self.get_state("input_boolean.mode_return_home") == "on":
            if new == "RW":
                self.mmess_woden = "Megan at Woden, R4 to Tugg79 " + self.get_state("sensor.tugg_to_home_79_homecheck") + " or R5 " + self.get_state("sensor.woden_to_home_r5_homecheck")
                self.notifier.notify(self.mmess_woden)
            elif new == "7X":
                self.notifier.notify(self.mmess_tugg_home)
            elif new == "TX":
                self.notifier.notify(self.mmess_tugg)
            elif new == "Cal":
                self.notifier.notify(self.mmess_cal)
            elif new == "Car":
                self.notifier.notify(self.mmess_car)
            elif new == "RC":
                self.notifier.notify(self.mmess_bus)

    def transport_staci(self, entity, attribute, old, new, kwargs):
        if self.get_state("input_boolean.mode_return_home") == "on":
            if new == "RC":
                self.notifier.notify(self.stmess_cit)
            if new == "RW":
                self.stmess_woden = "Staci at Woden, R4 to Tugg79 " + self.get_state("sensor.tugg_to_home_79_homecheck") + " or R5 " + self.get_state("sensor.woden_to_home_r5_homecheck")
                self.notifier.notify(self.stmess_woden)
            elif new == "7X":
                self.notifier.notify(self.stmess_tugg_home)
            elif new == "TX":
                self.notifier.notify(self.stmess_tugg)
            elif new == "Cal":
                self.notifier.notify(self.stmess_cal)
            elif new == "Central":
                self.notifier.notify(self.stmess_ctr)

