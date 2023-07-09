# Sim Rig Automations

Automate your presets and setup you Sim Racing rig for various games, cars, driving styles, key button mappings etc...

I'm sick of having to pre-select so many things to Drift or do Grip or Rally.  From Fanatec Settings, In Game Settings, Key Mapping (JoyToKey).  It becomes to constnat battle to try to get it right, and makes me avoid playing other racing styles as its too much setup.  This is my implementation to simplfy this and write a few scripts to automatically setup my environment for what I want. 



## main.py
`main.py` this main script will call the other scripts to setu pyour environment however you need.  You can make multiple copies of this adjusting the arguments or scripts that you need. 



##### JoyToKey
`JoyToKey.py` is a simple script that opens the app, and select the name of your preset. (Replace "Assetto Corsa - GT" with your preset name)
```
python joytokey.py "Assetto Corsa - GT"
```



##### Fanatec Control Panel
`fanatec_control_panel_preset.py` is a script to open fanatec control panel, navigate to the tuning tab and the select 1 of the 5 presets. 
To use this, simply call the script and pass in the preset number you would like it to select. 
```
python fanatec_control_panel_preset.py 2
```

##### Fanalab
STILL WORKING ON THIS, WILL REPLACE FANATEC CONTROL PANEL WHEN ITS FINISHED
`Fanalab.py` is still a work in progress, but hoping to open Fanalab, Navigate to the Game page, click the game you need, then click then double click the profile for that game.  It can do the first portion taking in the 1st arg for the game name, still working on getting the profile for the games loaded as an option. 
```
python fanalab2.py "Assetto Corsa"
```
Notes:  It has an array of game names, currently it cycles through the non hidden games, but a faster option may be to use the array to click the exact one you want instead. This will break if they add/remove any games from Fanalab though.  This is the current list of games in order as of 7/8/2023
```
Assetto Corsa
DiRT Rally 2.0
iRacing
Assetto Corsa Competizione
Automobilista
Automobilista 2
DiRT Rally
F1 2017
F1 2018
F1 2019
F1 2020
F1 2021
F1 22
Kart Kraft
Project Cars
Project Cars 2
RaceRoom Experience
rFactor
rFactor 2
GRID 2019
WRC Generations
```



##### Content Manager
STILL WORKING ON THIS, THIS WILL SET ALL PRESETS WITHIN ASSETTO CORSA / CONTENT MANAGEr
`CMPreset_to_ACINI.py` is a script to convert CMPreset (json style) config files to Assetto Corsa .ini files. This is only working for Audio and Video currently.   This way it can quickly select and copy over your audio/video presets into assetto corsa. 



