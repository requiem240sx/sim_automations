import subprocess
import time
import pyautogui
from pywinauto import Application
import os

# Set the paths to your Fanatec Tuning Menu executable and presets
fanatec_control_panel = r"C:\Program Files\Fanatec\Fanatec Wheel\ui\FanatecControlPanel.exe"
fanatec_control_pandel_directory = r"C:\Program Files\Fanatec\Fanatec Wheel\ui"


# Launch Fanatec Control Panel
os.chdir(fanatec_control_pandel_directory)
subprocess.Popen([fanatec_control_panel])
time.sleep(2) # Wait for the Fanatec Control Panel to Load



# Connect to the Fanatec Tuning Menu application
app = Application(backend="uia").connect(path=fanatec_control_panel)

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


# Click Tuning Menu Button
mouse_click(200, 400)
time.sleep(1)

# Click Setup 1
mouse_click(495, 190)
time.sleep(1)

# Click Setup 2
mouse_click(660, 190)
time.sleep(1)

# Click Setup 3
mouse_click(825, 190)
time.sleep(1)

# Click Setup 4
mouse_click(990, 190)
time.sleep(1)

# Click Setup 5
mouse_click(1155, 190)

