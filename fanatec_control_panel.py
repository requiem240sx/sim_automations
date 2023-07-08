import subprocess
import time
import pyautogui
from pywinauto import Application
import os
import sys

# Set the paths to your Fanatec Tuning Menu executable and presets
fanatec_control_panel = r"C:\Program Files\Fanatec\Fanatec Wheel\ui\FanatecControlPanel.exe"
fanatec_control_panel_directory = r"C:\Program Files\Fanatec\Fanatec Wheel\ui"

# Change to the Fanatec Control Panel directory
try:
    os.chdir(fanatec_control_panel_directory)
    print("Changed to Fanatec Control Panel directory successfully.")
except FileNotFoundError:
    print("Fanatec Control Panel directory not found. Please check the directory path.")
    sys.exit(1)

# Launch Fanatec Control Panel
try:
    subprocess.Popen([fanatec_control_panel])
    print("Fanatec Control Panel launched successfully.")
except FileNotFoundError:
    print("Fanatec Control Panel executable not found. Please check the file path.")
    sys.exit(1)

time.sleep(2)  # Wait for the Fanatec Control Panel to load

# Connect to the Fanatec Tuning Menu application
try:
    app = Application(backend="uia").connect(path=fanatec_control_panel)
    print("Connected to the Fanatec Tuning Menu application.")
except Exception as e:
    print("Failed to connect to the Fanatec Tuning Menu application:", e)
    sys.exit(1)

# Get the main window of the application
main_window = app.window()

def mouse_click(x, y):
    # Move the application window to the front (optional)
    main_window.set_focus()

    # Get the position of the application window
    window_rect = main_window.rectangle()

    # Calculate the absolute coordinates of the point within the window
    absolute_x = window_rect.left + x
    absolute_y = window_rect.top + y

    # Click the specified point using pyautogui
    pyautogui.click(x=absolute_x, y=absolute_y)

# Get the setup number from command-line argument
if len(sys.argv) > 1:
    try:
        setup_number = int(sys.argv[1])
    except ValueError:
        print("Invalid setup number. Please provide a valid integer.")
        sys.exit(1)
else:
    setup_number = 1  # Default to setup 1 if no argument is provided

# Define the setup click coordinates
setup_coordinates = {
    1: (495, 190),
    2: (660, 190),
    3: (825, 190),
    4: (990, 190),
    5: (1155, 190)
}

# Click Tuning Menu Button
mouse_click(200, 400)
time.sleep(1)

# Click the specified setup based on the setup number
if setup_number in setup_coordinates:
    click_x, click_y = setup_coordinates[setup_number]
    mouse_click(click_x, click_y)
else:
    print("Invalid setup number. Please choose a number between 1 and 5.")
