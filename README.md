# Sim Rig Automations

Automate your presets and setup you Sim Racing rig for various games, cars, driving styles, key button mappings etc...

I'm sick of having to pre-select so many things to Drift or do Grip or Rally.  From Fanatec Settings, In Game Settings, Key Mapping (JoyToKey).  It becomes to constnat battle to try to get it right, and makes me avoid playing other racing styles as its too much setup.  This is my implementation to simplfy this and write a few scripts to automatically setup my environment for what I want.

## Using with Claude Code

When using Claude Code with this repository, run the following command to load the project context:

```bash
claude
/context
```

This will load the AI documentation from the `ai_docs` directory and help Claude understand the project structure and conventions.


## main.py
`main.py` this main script will call the other script(s) to setup your environment however you need.  You can make multiple copies of this adjusting the arguments or scripts that you need, then simpy make a shortcut you can double click to run. 



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
`Fanalab.py` Will navigate to the Game page, click the game you want, then double click the profile for that game. 
```
python .\fanalab.py "Assetto Corsa" "Grip-V2"
```
Note:  It has an array of game names, currently it cycles through the non hidden games, but a faster option may be to use the array to click the exact one you want instead. This will break if they add/remove any games from Fanalab though.  This is the current list of games in order as of 7/8/2023
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
STILL WORKING ON THIS, THIS WILL SET ALL PRESETS WITHIN CONTENT MANAGER / ASSETTO CORSA
`cm_preset.py` is a script that you can pass in your presets, and it will go select them all for you. 

```
python cm_preset.py --ac_audio_preset "VR-V1" --ac_video_preset "HQ-HDR" --cm_preset "HQ-GripV3"

# Info
--ac_audio_preset (Add preset name that is in assetto corsa audio settings)
--ac_video_preset (Add preset name that is in assetto corsa vieo settings)
 --cm_preset (Add preset name that is in content manager settings)
```



