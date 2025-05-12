
# Architecture Principles

1. **Modularity**: Each application has its own script that can be used independently
2. **Command-line driven**: Scripts accept arguments to specify which presets to use
3. **Orchestration**: A main script coordinates calls to the application-specific scripts
4. **Flexibility**: Users can create shortcuts with specific arguments for different scenarios

# Core Applications

- **JoyToKey**: Handles button mapping for different steering wheels
- **Fanatec Control Panel**: Manages force feedback and wheel settings
- **Fanalab**: Controls game-specific profiles
- **Content Manager**: Configures Assetto Corsa game settings

# Key Files and Their Purposes

- **main.py**: Orchestrates calls to application-specific scripts
- **joytokey.py**: Selects presets in JoyToKey for button mapping, 
- **fanatec_control_panel_preset.py**: Sets force feedback profiles in Fanatec Control Panel
- **fanalab.py**: Selects game profiles in Fanalab
- **cm_presets.py**: Configures Content Manager/Assetto Corsa settings
- **CMPreset_to_ACINI_converter.py**: Utility for converting Content Manager presets to Assetto Corsa INI