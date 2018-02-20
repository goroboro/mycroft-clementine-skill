import sys
import dbus
import glib
import os
import psutil
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import subprocess

__author__ = 'roboro'


LOGGER = getLogger(__name__)

class GooglePlayMusicPlayerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(GooglePlayMusicPlayerSkill, self).__init__(name="GooglePlayMusicPlayerSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        # set the downer variable to your music-player is maybe enough for make it working
        self.playerName="google-play-music-desktop-player"
        
        internals_googleplay_play_skill_intent = IntentBuilder("GooglePlayPlayKeywordIntent").\
            require("GooglePlayPlayKeyword").build()
        self.register_intent(internals_googleplay_play_skill_intent, self.handle_internals_googleplay_play_skill_intent)

        internals_googleplay_jump_forward_skill_intent = IntentBuilder("GooglePlayJumpForwardKeywordIntent").\
            require("GooglePlayJumpKeyword").require("nrOfSongs").require("GooglePlayJumpForwardKeyword").build()
        self.register_intent(internals_googleplay_jump_forward_skill_intent, self.handle_internals_googleplay_jumpForward_skill_intent)

        internals_googleplay_jump_backward_skill_intent = IntentBuilder("GooglePlayJumpBackwardKeywordIntent").\
            require("GooglePlayJumpKeyword").require("nrOfSongs").require("GooglePlayJumpBackwardKeyword").build()
        self.register_intent(internals_googleplay_jump_backward_skill_intent, self.handle_internals_googleplay_jumpBackward_skill_intent)
                
        internals_googleplay_stop_skill_intent = IntentBuilder("GooglePlayStopKeywordIntent").\
            require("GooglePlayStopKeyword").build()
        self.register_intent(internals_googleplay_stop_skill_intent, self.handle_internals_googleplay_stop_skill_intent)
        
        internals_googleplay_next_skill_intent = IntentBuilder("GooglePlayNextKeywordIntent").\
            require("GooglePlayNextKeyword").build()
        self.register_intent(internals_googleplay_next_skill_intent, self.handle_internals_googleplay_next_skill_intent)

        internals_googleplay_previous_skill_intent = IntentBuilder("GooglePlayPreviousKeywordIntent").\
            require("GooglePlayPreviousKeyword").build()
        self.register_intent(internals_googleplay_previous_skill_intent, self.handle_internals_googleplay_previous_skill_intent)
        
        internals_googleplay_pause_skill_intent = IntentBuilder("googleplayPauseKeywordIntent").\
            require("googleplayPauseKeyword").build()
        self.register_intent(internals_googleplay_pause_skill_intent, self.handle_internals_googleplay_pause_skill_intent)


    def handle_internals_googleplay_play_skill_intent(self, message):    
	
            self.speak_dialog("googleplay.play")
            #print('yes')

	    def runplay(bus):
        	 remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2")
        	 remote_object.Play(dbus_interface = "org.mpris.MediaPlayer2.Player")	
	    
            
        
            def runprocandplay():
           	#cmdstring = "googleplay %s %s %s" % ('-p' '-k' '0')
           	#os.system(cmdstring)
           	subprocess.call([self.playerName])
           	bus = dbus.SessionBus()
           	remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2")
           	remote_object.Play(dbus_interface = "org.mpris.MediaPlayer2.Player")
   
            bus = dbus.SessionBus()
            if bus.request_name("org.mpris.MediaPlayer2."+self.playerName):
                runplay(bus)
            else:
                runprocandplay()

    def handle_internals_googleplay_stop_skill_intent(self, message):        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2") 
        remote_object.Stop(dbus_interface = "org.mpris.MediaPlayer2.Player")
        
        self.speak_dialog("googleplay.stop")
    
    def handle_internals_googleplay_next_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2") 
        remote_object.Next(dbus_interface = "org.mpris.MediaPlayer2.Player")
        
        self.speak_dialog("googleplay.next")
        
    def handle_internals_googleplay_jumpForward_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2")
        properties_manager = dbus.Interface(remote_object, 'org.freedesktop.DBus.Properties')
        nrOfSongs = message.data.get("nrOfSongs")
        try:
            parsedNrOfSongs = int(nrOfSongs)
            i = 0;
            while(parsedNrOfSongs>i):
                if(properties_manager.Get('org.mpris.MediaPlayer2.Player', 'CanGoPrevious')):
                    remote_object.Next(dbus_interface = "org.mpris.MediaPlayer2.Player")
                    i+=1
            self.speak("Jumped "+nrOfSongs+" songs forward")
        except ValueError:
            self.speak("sorry, was not able to parse the amount of songs i should go forward. Your wrong nr was: "+nrOfSongs)
    
    def handle_internals_googleplay_jumpBackward_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2")
        properties_manager = dbus.Interface(remote_object, 'org.freedesktop.DBus.Properties')
        nrOfSongs = message.data.get("nrOfSongs")
        try:
            parsedNrOfSongs = int(nrOfSongs)
            i = 0;
            while(parsedNrOfSongs>i):
                if(properties_manager.Get('org.mpris.MediaPlayer2.Player', 'CanGoPrevious')):
                    remote_object.Previous(dbus_interface = "org.mpris.MediaPlayer2.Player")
                    i+=1
            self.speak("Jumped "+nrOfSongs+" songs backward")
        except ValueError:
            self.speak("sorry, was not able to parse the amount of songs i should go backward. Your wrong nr was: "+nrOfSongs)

        
    def handle_internals_googleplay_previous_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2") 
        remote_object.Previous(dbus_interface = "org.mpris.MediaPlayer2.Player")
        
        self.speak_dialog("googleplay.previous")     

    def handle_internals_googleplay_pause_skill_intent(self, message):
        
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.mpris.MediaPlayer2."+self.playerName,"/org/mpris/MediaPlayer2") 
        remote_object.PlayPause(dbus_interface = "org.mpris.MediaPlayer2.Player")
        
        self.speak_dialog("googleplay.pause")     
        
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return GooglePlayMusicPlayerSkill()
