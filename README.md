# mycroft-google-play-desktop-player-skill
This skill integrates the Linux version of the Google Play Music Desktop Player with Mycroft which enables users to Play Local Music.

See: https://www.googleplaymusicdesktopplayer.com/

It is forked from the mycroft-clementine-player-plasma-skill and works in a similiar way.

It could be that the plugin make conflicts with the amarok and clementine versions of the same skill because of the same commands, so you propaply have to decide what skill you need or you may need to modify the vocab for this skill.


#### Installation of skill:
* Download or Clone Git
* Create /opt/mycroft/skills folder if it does not exist
* Extract Downloaded Skill into a folder. "mycroft-google-play-desktop-player-skill". (Clone does not require this step)
* Copy the mycroft-internals-plasma-skill folder to /opt/mycroft/skills/ folder

#### Installation of requirements:
##### Fedora: 
- sudo dnf install dbus-python
- From terminal: cp -R /usr/lib64/python2.7/site-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib64/python2.7/site-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### Kubuntu / KDE Neon: 
- sudo apt install python-dbus
- From terminal: cp -R /usr/lib/python2.7/dist-packages/dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/
- From terminal: cp /usr/lib/python2.7/dist-packages/_dbus* /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/

##### For other distributions:
- Python Dbus package is required and copying the Python Dbus folder and lib from your system python install over to /home/$USER/.virtualenvs/mycroft/lib/python2.7/site-packages/.

##### How To Use: 
###### Play Music/Song
- "Hey Mycroft, play music"
- "Hey Mycroft, play song"

###### Pause Music/Song
- "Hey Mycroft, pause music"
- "Hey Mycroft, pause song"

###### Stop Music/Song
- "Hey Mycroft, stop music"
- "Hey Mycroft, stop song"

###### Next Song
- "Hey Mycroft, next song"

###### Previous Song
- "Hey Mycroft, previous song"

###### Jump forward
- "Hey Mycroft, jump 3 songs forward"
- "Hey Mycroft, go 8 forward"

###### Jump backward
- "Hey Mycroft, jump 10 songs back"
- "Hey Mycroft, go 4 backward"
- "Hey Mycroft, go 22 back"

## Current state

Working features:
* Play Music
* Pause Music
* Stop Music
* Next Song
* Previous Song

Known issues:
* None

TODO:
* None
