# Overview

A Python automation framework for sim racing that configures multiple applications (JoyToKey, Fanatec Control Panel, Fanalab, Content Manager) through modular scripts. Enables quick switching between racing setups (drift, grip, rally) and display modes without manual reconfiguration.

## Project Context

READ the README.md.
THEN read the ai_docs/* files for documentation, particularly:
- ai_docs/development_guidelines.md (Main guidelines for development)
- ai_docs/project_overview.md (Project architecture and core concepts)

Sim Automations is a modular Python project that automates configuration of simulation racing setups across multiple applications. The project helps users switch between different racing styles (grip racing vs. drift) and display options (TV vs. VR headset) by selecting pre-configured presets in various sim racing applications.

## Assistant Capabilities

As an assistant for this project, you should:

1. **Understand the codebase structure and purpose** of each module
2. **Maintain modularity** when suggesting improvements or new features
3. **Recommend code organization improvements** including:
   - Package structure with proper imports
   - Configuration management
   - Error handling and logging
   - Testing strategies
4. **Help implement new application integrations** while following existing patterns
5. **Suggest efficiency improvements** without compromising readability
6. **Consider the user experience** for both developers and end users
7. **Preserve backward compatibility** with existing scripts and shortcuts

## Technical Considerations

When providing assistance:

1. **UI Automation**: Scripts use pywinauto and pyautogui for GUI interaction
2. **Configuration**: Currently uses command-line arguments but may benefit from config files
3. **Error Handling**: Need robust handling for applications that don't respond
4. **Portability**: Scripts should work on Windows machines with varying display setups
5. **Performance**: Scripts should execute quickly to minimize setup time
6. **Usability**: Consider developers and non-technical end users

## Do Not

1. Don't suggest converting to a monolithic application
2. Don't remove the ability to run individual scripts independently
3. Don't over-engineer solutions beyond the project's scope
4. Don't introduce dependencies that would make installation difficult

When making recommendations, consider the overall architecture and specific goals of making the system more stable, scalable, and maintainable while preserving its modular design.

Simply output "I've setup the context for the repo" once you have read and understand the above. 