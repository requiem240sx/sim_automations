# sim_automations
Automate Sim Racing rig setup tasks for various games, cars, driving styles etc...

I'm sick of having to pre-select a million things to Drift or do F1 or do Grip.  For Fanatec Settings, In Game Settings, and Key Mapping (JoyToKey).  It becomes to constantly try to get it right.  This is my implementation to simplfy this and write scripts to automatically setup my environment for what I want. 

#### JoyToKey
`JoyToKey.py` is a simple script that opens the app, and will select the name of your preset. 

#### Fanalab
`Fanalab.py` is still a work in progress, but hoping to open Fanalab, Navigate to the Game page, click a game, then click then double click the profile. 

#### Content Manager
`CMPreset_to_ACINI.py` is a script to convert CMPreset (json style) config files to Assetto Corsa .ini files. This is only working for Audio and Video currently.   This way it can quickly select and copy over your audio/video presets into assetto corsa. 



#### Fanatec Control Panel
`fanatec_control_panel.py` is a script to open fanatec control panel, navigate to the tuning tab and the select 1 of the 5 presets. 
To use this, simply call the script and pass in the preset number you would like it to select. 
Example: `python .\fanatec_control_panel_preset.py 2`
