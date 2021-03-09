#
#The aim of this is to control the travel functions for individuals

# Version 3 - July 2019

import appdaemon.plugins.hass.hassapi as hass
import time
import globals

class Travel_Messages(hass.Hass):

    away_flag = "off"

    s_loc = "home"
    m_loc = "home"
    st_loc = "home"
    d_loc = "home"

    sendmess = ""
    #the request timer will set how often to request gps notifications on returning to the house

    smess = "Simon is currently at "
    mmess = "Megan is currently at "
    stmess = "Staci is currently at "
    dmess = "Delia is currently at "
    hmess = "The best route home is via "
    wmess = "The best route to the city is via "
    umess = "The best route to City West is via "

    t_mess = " which is approx "
    e_mess = " minutes away via "

    def initialize(self):

        # bring in the messaging module
        self.notifier = self.get_app('messaging')

        self.listen_state(self.tester, "input_boolean.message_test")

        # car connection messages
        self.listen_state(self.con_car, "binary_sensor.drive_meg")
        self.listen_state(self.con_car, "binary_sensor.drive_simon")
        # megan car or walkbus
        self.listen_state(self.meg_trav, "binary_sensor.megan_car")
        self.listen_state(self.meg_trav, "binary_sensor.megan_walk_bus")
        # simon car or walkbus
        self.listen_state(self.sim_trav, "binary_sensor.simon_car")
        self.listen_state(self.sim_trav, "binary_sensor.simon_walk_bus")
        # staci car or walkbus
        self.listen_state(self.sta_trav, "binary_sensor.staci_car")
        self.listen_state(self.sta_trav, "binary_sensor.staci_walk_bus")
        # delia car or walkbus
        self.listen_state(self.del_trav, "binary_sensor.delia_car")
        self.listen_state(self.del_trav, "binary_sensor.delia_walk_bus")

        # ha proximity code
        self.listen_state(self.arr_prox, "proximity.home_meg")
        self.listen_state(self.arr_prox, "proximity.home_simon")
        #these maybe needed if the girls starting driving - just uncomment, code supports
        #self.listen_state(self.arr_prox, "proximity.home_staci")
        #self.listen_state(self.arr_prox, "proximity.home_delia")

        # car away
        self.listen_state(self.car_away, "input_boolean.presence_holiday")
        # keep track of locations
        self.listen_state(self.sim_loc, "person.simon")
        self.listen_state(self.meg_loc, "person.megan")
        self.listen_state(self.sta_loc, "person.staci")
        self.listen_state(self.del_loc, "person.delia")


    def tester(self, entity, attribute, old, new, kwargs):
        self.personal_gps('sgps', 'turn_off')
        self.log("requesting close update for Simon")


    def car_away(self, entity, attribute, old, new, kwargs):
        self.away_flag = new

    ###
    #   These look at if people are home, and if they leave it turns off their fans
    ###

    def sim_loc(self, entity, attribute, old, new, kwargs):
        self.s_loc = new
        if new != 'home' and self.m_loc != 'home':
            self.turn_off("fan.master_fan")
        else:
            self.personal_gps('sgps', 'turn_off')
    
    def meg_loc(self, entity, attribute, old, new, kwargs):
        self.m_loc = new
        if new != 'home' and self.s_loc != 'home':
            self.turn_off("fan.master_fan")
        else:
            self.personal_gps('mgps', 'turn_off')

    def sta_loc(self, entity, attribute, old, new, kwargs):
        self.st_loc = new
        if new != 'home':
            self.turn_off("fan.staci_s_fan")
        else:
            self.personal_gps('stgps', 'turn_off')

    def del_loc(self, entity, attribute, old, new, kwargs):
        self.d_loc = new
        if new != 'home':
            self.turn_off("fan.delia_s_fan")
        else:
            self.personal_gps('dgps', 'turn_off')

    ###
    #   This controls various flags and actions through the the proximity platform
    ###
    
    def arr_prox(self, entity, attribute, old, new, kwargs):

        self.sendmess = ""
        prox = -1
        dir_trav = ""
        gps_person = ""
        pname = ""
        sdrive = self.get_state("input_boolean.simon_outback")
        mdrive = self.get_state("input_boolean.megan_outback")
        stdrive = self.get_state("input_boolean.staci_outback")
        ddrive = self.get_state("input_boolean.delia_outback")
        self.log(entity + " " + new + " call ")
        self.log(sdrive + " s " + mdrive + " m ")

        if new != 'not set':
            self.log("past not set")
            if entity == 'proximity.home_simon':    
                self.log("past knowing it is simon " + sdrive ) 
                if sdrive == 'on':
                    prox = float(new)
                    dir_trav = self.get_state("sensor.s_travel_direction")
                    gps_person = "sgps"
                    pname = "Simon"
                    self.log(str(prox) + " set")
            elif entity == 'proximity.home_meg':
                if mdrive == 'on':
                    prox = float(new)
                    dir_trav = self.get_state("sensor.m_travel_direction")
                    gps_person = "mgps"
                    pname = "Megan"
                    self.log(str(prox) + " set")
            elif entity == 'proximity.home_staci':
                if stdrive == 'on':
                    prox = float(new)
                    dir_trav = self.get_state("sensor.st_travel_direction")
                    gps_person = "stgps"
                    pname = "Staci"
            elif entity == 'proximity.home_delia':
                if ddrive == 'on':
                    prox = float(new)
                    dir_trav = self.get_state("sensor.d_travel_direction")
                    gps_person = "dgps"
                    pname = "Delia"

            self.log(str(prox) + " " + entity + " " + dir_trav)
            if prox != -1:
                #holiday
                if prox > 50:
                    if self.get_state("input_boolean.presence_holiday") == 'off':
                        self.turn_on('input_boolean.presence_holiday')
                        self.sendmess = "Car is going outside Canberra Region, messages around driving disabled"
                #returning to canberra
                elif prox < 50:
                    if self.get_state("input_boolean.presence_holiday") == 'on':
                        self.turn_off('input_boolean.presence_holiday')
                        self.sendmess = "Car has returned to the Canberra Region, messages around driving enabled"

                #close tracking
                if dir_trav == "towards":
                    if prox <= 4 and prox > 1:
                        # proximity under 5 kilometres, and arriving by car - start requesting gps updates
                        self.personal_gps(gps_person, 'turn_on')
                        self.log("requesting close update for " + pname)
                    elif prox <= 1:
                        # proximity under 1 kilometres, and arriving by car - open garage door
                        if self.get_state("input_boolean.garage_just") != "on":
                            # if you opened it for someone else in the last 5 minutes, don't open it again
                            self.call_service("cover/open_cover", entity_id = "cover.near_garage_door")
                            self.set_state("input_boolean.garage_just", state="on")
                            self.sendmess = "Opening the Garage Door for " + pname + "arriving by car (Proximity)"
                    else:
                        # proximity over 5 kilometres, turn off the high accuracy gps
                        self.personal_gps(gps_person, 'turn_off')

        #send the message
        if self.sendmess != "":
            self.notifier.notify(self.sendmess)

    ###
    #   when turned on, will continue to request gps updates for tracking close to the house
    ###

    def personal_gps(self, person, onoffval):
        # gps will be requested more often to ensure the garage door entry is more consistent
        self.log("request accurate gps " + onoffval + " for " + person)
        self.notifier.notify(mess=person, onoff=onoffval)

    ###
    #   watches the connection to the car and send the appropriate message
    ###

    def con_car(self, entity, attribute, old, new, kwargs):
        
        self.sendmess = ""

        # only do this if the car is in the canberra region
        if self.away_flag == "off":

            if entity == 'binary_sensor.drive_meg' and new == 'on':
                # build a message for Meg being in the car
                self.sendmess = "Megan is now driving, use text messages if you need to contact her. " + "\n"
                # if at home, show the distances to others and to work
                if self.m_loc != "home":
                    self.sendmess += self.hmess + self.get_state("sensor.m_to_h_route") + "\n"
                else:
                    self.sendmess += self.wmess + self.get_state("sensor.m_to_w_route") + "\n"

                if self.s_loc != "home": # if not at home, show directions if they are more than 5 minutes away
                    if int(self.get_state("sensor.waze_meg_to_simon")) >= 5:
                        self.sendmess += self.smess + self.s_loc + self.t_mess + self.get_state("sensor.waze_meg_to_simon") + self.e_mess + self.get_state("sensor.m_to_s_route") + "\n"
                if self.st_loc != "home":
                    if int(self.get_state("sensor.waze_meg_to_staci")) >= 5:
                        self.sendmess += self.stmess + self.st_loc + self.t_mess + self.get_state("sensor.waze_meg_to_staci") + self.e_mess + self.get_state("sensor.m_to_st_route") + "\n"
                if self.d_loc != "home":
                    if int(self.get_state("sensor.waze_meg_to_delia")) >= 5:
                        self.sendmess += self.dmess + self.d_loc + self.t_mess + self.get_state("sensor.waze_meg_to_delia") + self.e_mess + self.get_state("sensor.m_to_d_route") + "\n"
            
            elif entity == 'binary_sensor.drive_simon' and new == 'on':
                # build a message for Meg being in the car
                self.sendmess = "Simon is now driving, use text messages if you need to contact him. " + "\n"
                # if at home, show the distances to others and to work
                if self.s_loc != "home":
                    self.sendmess += self.hmess + self.get_state("sensor.s_to_h_route") + "\n"
                else:
                    self.sendmess += self.umess + self.get_state("sensor.s_to_w_route") + "\n"

                if self.m_loc != "home": # if not at home, show directions if they are more than 5 minutes away
                    if int(self.get_state("sensor.waze_meg_to_simon")) >= 5:
                        self.sendmess += self.mmess + self.m_loc + self.t_mess + self.get_state("sensor.waze_meg_to_simon") + self.e_mess + self.get_state("sensor.m_to_s_route") + "\n"
                if self.st_loc != "home":
                    if int(self.get_state("sensor.waze_simon_to_staci")) >= 5:
                        self.sendmess += self.stmess + self.st_loc + self.t_mess + self.get_state("sensor.waze_simon_to_staci") + self.e_mess + self.get_state("sensor.s_to_st_route") + "\n"
                if self.d_loc != "home":
                    if int(self.get_state("sensor.waze_simon_to_delia")) >= 5:
                        self.sendmess += self.dmess + self.d_loc + self.t_mess + self.get_state("sensor.waze_simon_to_delia") + self.e_mess + self.get_state("sensor.s_to_d_route") + "\n"
                
            #send the message
            if self.sendmess != "":
                self.notifier.notify(self.sendmess)


    ###
    #   These set the input select to what we believe is the correct function at the time.
    ###
    def meg_trav(self, entity, attribute, old, new, kwargs):
        
        self.sendmess = ""

        ### Showing as just arrived home
        if self.get_state("input_select.trav_megan") != 'Home' and self.get_state("person.megan") == 'home' and self.get_state('binary_sensor.drive_meg') == 'off':
            # if both of these are true then Meg must have just arrived home (as the sensors are only true when not_home)
            # check if by car or by foot, and unlock the appropriate door
            if self.get_state("input_select.trav_megan") == "Car":
                # arrived by car
                # unlock the garage rear entry door
                #self.turn_off("input_boolean.gdoor")
                self.sendmess = 'Welcome home Megan, returning via car.' 
            elif self.get_state("input_select.trav_megan") == "Walk":
                # arrived by walking
                # unlock the front door
                #self.turn_off("input_boolean.fdoor")
                self.sendmess = 'Welcome home Megan, returning via foot.'

            # set Megan to being at home
            self.set_state("input_select.trav_megan", state="Home")

        ### showing in the car (may be called when a passenger or the driver, but as it only sets the state no issue)
        elif self.get_state("binary_sensor.megan_car") == 'on':
            
            # set Megan to being in the car, either by herself or in the car with Simon)
            self.set_state("input_select.trav_megan", state="Car")

        ### Showing walking or catching the bus, nothing specific here now 
        elif self.get_state("binary_sensor.megan_walk_bus") == 'on':
            self.set_state("input_select.trav_megan", state="Walk")
    
        #send the message
        if self.sendmess != "":
            self.notifier.notify(self.sendmess)
        
    

    def sim_trav(self, entity, attribute, old, new, kwargs):
        
        self.sendmess = ""
        
        ### Showing as just arrived home
        if self.get_state("input_select.trav_simon") != 'Home' and self.get_state("person.simon") == 'home' and self.get_state('binary_sensor.drive_simon') == 'off':
            # if both of these are true then Simon must have just arrived home (as the sensors are only true when not_home)
            # check if by car or by foot, and unlock the appropriate door
            if self.get_state("input_select.trav_simon") == "Car":
                # arrived by car
                # unlock the garage rear entry door
                #self.turn_off("input_boolean.gdoor")
                self.sendmess = 'Welcome home Simon, returning via car.' 
            elif self.get_state("input_select.trav_simon") == "Walk":
                # arrived by walking
                # unlock the front door
                #self.turn_off("input_boolean.fdoor")
                self.sendmess = 'Welcome home Simon, returning via foot.' 

            # set Simon to being at home
            self.set_state("input_select.trav_simon", state="Home")

        ### showing in the car (may be called when a passenger or the driver, but as it only sets the state no issue)
        elif self.get_state("binary_sensor.simon_car") == 'on':

            # set Simon to being in the car, either by herself or in the car with Megan)
            self.set_state("input_select.trav_simon", state="Car")

        ### Showing walking or catching the bus, nothing specific here now 
        elif self.get_state("binary_sensor.simon_walk_bus") == 'on':
            self.set_state("input_select.trav_simon", state="Walk")

        #send the message
        if self.sendmess != "":
            self.notifier.notify(self.sendmess)

    def sta_trav(self, entity, attribute, old, new, kwargs):
        
        self.sendmess = ""

        ### Showing as just arrived home
        if self.get_state("input_select.trav_staci") != 'Home' and self.get_state("person.staci") == 'home':
            # if both of these are true then Staci must have just arrived home (as the sensors are only true when not_home)
            # check if by car or by foot, and unlock the appropriate door
            if self.get_state("input_select.trav_staci") == "Car":
                # arrived by car
                # unlock the garage rear entry door
                #self.turn_off("input_boolean.gdoor")
                self.sendmess = 'Welcome home Staci, returning via car.' 
            elif self.get_state("input_select.trav_staci") == "Walk":
                # arrived by walking
                # unlock the front door
                #self.turn_off("input_boolean.fdoor")
                self.sendmess = 'Welcome home Staci, returning via foot.' 

            # set Staci to being at home
            self.set_state("input_select.trav_staci", state="Home")

        ### showing in the car (may be called when a passenger or the driver, but as it only sets the state no issue)
        elif self.get_state("binary_sensor.staci_car") == 'on':           

            # set Staci to being in the car, either by herself or in the car with Simon/Megan)
            self.set_state("input_select.trav_staci", state="Car")

        ### Showing walking or catching the bus, nothing specific here now 
        elif self.get_state("binary_sensor.staci_walk_bus") == 'on':

            # set Megan to being walking
            self.set_state("input_select.trav_staci", state="Walk")
        

        #send the message
        if self.sendmess != "":
            self.notifier.notify(self.sendmess)


    def del_trav(self, entity, attribute, old, new, kwargs):
        
        self.sendmess = ""

        ### Showing as just arrived home
        if self.get_state("input_select.trav_delia") != 'Home' and self.get_state("person.delia") == 'home':
            # if both of these are true then Delia must have just arrived home (as the sensors are only true when not_home)
            # check if by car or by foot, and unlock the appropriate door
            if self.get_state("input_select.trav_delia") == "Car":
                # arrived by car
                # unlock the garage rear entry door
                #self.turn_off("input_boolean.gdoor")
                self.sendmess = 'Welcome home Delia, returning via car.' 
            elif self.get_state("input_select.trav_delia") == "Walk":
                # arrived by walking
                # unlock the front door
                #self.turn_off("input_boolean.fdoor")
                self.sendmess = 'Welcome home Delia, returning via foot.' 

            # set Delia to being at home
            self.set_state("input_select.trav_delia", state="Home")

        ### showing in the car (may be called when a passenger or the driver, but as it only sets the state no issue)
        elif self.get_state("binary_sensor.delia_car") == 'on':

            # set Delia to being in the car, either by herself or in the car with Simon/Megan)
            self.set_state("input_select.trav_delia", state="Car")

        ### Showing walking or catching the bus, nothing specific here now 
        elif self.get_state("binary_sensor.delia_walk_bus") == 'on':

            # set Delia to being walking
            self.set_state("input_select.trav_delia", state="Walk")
        
        #send the message
        if self.sendmess != "":
            self.notifier.notify(self.sendmess)
        



