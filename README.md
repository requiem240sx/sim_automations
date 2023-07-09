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
`Fanalab.py` is still a work in progress, but hoping to open Fanalab, Navigate to the Game page, click a game, then click then double click the profile. 

##### Content Manager
STILL WORKING ON THIS, THIS WILL SET ALL PRESETS WITHIN ASSETTO CORSA / CONTENT MANAGEr
`CMPreset_to_ACINI.py` is a script to convert CMPreset (json style) config files to Assetto Corsa .ini files. This is only working for Audio and Video currently.   This way it can quickly select and copy over your audio/video presets into assetto corsa. 



