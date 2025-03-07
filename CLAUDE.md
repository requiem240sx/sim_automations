# CLAUDE.md - Guidelines for Sim Automations Project

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

## Notes
This project interfaces with external applications through GUI automation - changes to those applications may require updates to the automation scripts.