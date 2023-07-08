import subprocess
import time
import os
from pywinauto import Application

# Define constants
OPEN_JOYTOKEY_PATH = r"C:\Program Files (x86)\JoyToKey\JoyToKey.exe"
SLEEP_DURATION = 1  # Duration to wait for an application to load
JOYTOKEY_LIST_ITEM = "Assetto Corsa - Drift"

def launch_application(app_path):
    """Launches an application at the specified path."""
    try:
        subprocess.Popen([app_path])
        print(f"Successfully launched {app_path}")
    except Exception as e:
        print(f"Failed to launch {app_path}: {e}")

def connect_to_application(app_path):
    """Connects to an application and returns its main window."""
    try:
        app = Application(backend="uia").connect(path=app_path)
        main_window = app.window()
        print(f"Successfully connected to {app_path}")
        return main_window
    except Exception as e:
        print(f"Failed to connect to {app_path}: {e}")

def focus_on_window(window):
    """Sets focus on the specified window."""
    try:
        window.set_focus()
        print("Window focus set")
    except Exception as e:
        print(f"Failed to set focus: {e}")

def main():
    # Launch JoyToKey 
    launch_application(OPEN_JOYTOKEY_PATH)
    time.sleep(SLEEP_DURATION)  # Wait for the application to load

    # Connect to the application
    main_window = connect_to_application(OPEN_JOYTOKEY_PATH)
    time.sleep(SLEEP_DURATION)  # Wait for the connection to establish

    # Set focus on the main window
    focus_on_window(main_window)

    # Get the parent list control using AutomationId
    list_control = main_window.child_window(auto_id="395730", control_type="List")

    # Get the list item and click on it
    list_item = list_control.get_item(JOYTOKEY_LIST_ITEM)
    list_item.click_input()
    print("JoyToKey Profile: " + JOYTOKEY_LIST_ITEM)

if __name__ == "__main__":
    main()
