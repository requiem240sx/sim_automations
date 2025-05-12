# Guidelines for Sim Automations Project

## Project Overview

Automation scripts for sim racing setup configurations, using PyAutoGUI and PyWinAuto for GUI automation across JoyToKey, Fanatec Control Panel, Fanalab, and Content Manager.

## Commands

- Run main script: `python main.py`
- Run specific module: `python <module_name>.py`

## Code Style Guidelines

- **Imports**: Standard library first, then third-party, then local modules
- **Formatting**: 4-space indentation, 120 character line limit
- **Types**: Use type hints for function parameters and return values
- **Naming**: 
  - snake_case for variables and functions
  - CamelCase for classes
  - UPPERCASE for constants
- **Error Handling**: Use try/except blocks for GUI interactions that may fail
- **Documentation**: Docstrings for modules and functions, inline comments for complex operations
- **GUI Automation**: Always include timing delays between actions to ensure reliability

## Technical Considerations

1. **UI Automation**: Scripts use pywinauto and pyautogui for GUI interaction
2. **Configuration**: Currently uses command-line arguments but may benefit from config files
3. **Error Handling**: Need robust handling for applications that don't respond
4. **Portability**: Scripts should work on Windows machines with varying display setups
5. **Performance**: Scripts should execute quickly to minimize setup time
6. **Usability**: Consider developers and non-technical end users

## Contributing Guidelines

When contributing to this project:

1. **Maintain modularity** when implementing new features
2. **Preserve backward compatibility** with existing scripts and shortcuts
3. **Follow existing patterns** when adding new application integrations
4. **Consider the user experience** for both developers and end users

## Notes

This project interfaces with external applications through GUI automation - changes to those applications may require updates to the automation scripts.

## What Not To Do

1. Don't convert to a monolithic application
2. Don't remove the ability to run individual scripts independently
3. Don't over-engineer solutions beyond the project's scope
4. Don't introduce dependencies that would make installation difficult