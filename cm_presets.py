import subprocess
import time
import os
import argparse
import pyautogui
from pywinauto import Application
import keyboard

# Define constants
CONTENT_MANAGER_PATH = r"C:\Users\dominic\Documents\asseto_mods\Content Manager.exe"
SLEEP_DURATION = 1  # Duration to wait for an application to load

def launch_application(app_path):
    """Launches an application at the specified path."""
    try:
        subprocess.Popen([app_path])
        print(f"Content Manager - Successfully launched {app_path}")
    except Exception as e:
        print(f"Content Manager - Failed to launch {app_path}: {e}")

def connect_to_application(app_path):
    """Connects to an application and returns its main window."""
    try:
        app = Application(backend="uia").connect(path=app_path)
        main_window = app.window()
        print(f"Content Manager - Successfully connected to {app_path}")
        return main_window
    except Exception as e:
        print(f"Content Manager - Failed to connect to {app_path}: {e}")

def focus_on_window(window):
    """Sets focus on the specified window."""
    try:
        window.set_focus()
        print("Content Manager - Window focus set")
    except Exception as e:
        print(f"Content Manager - Failed to set focus: {e}")


def hover_over_first_item(menu):
    # Click to open the dropdown
    menu.click_input()
    time.sleep(1)  # Let the dropdown expand

    # Now, find the first available child element
    first_item = menu.children()[0]

    # Get the mid point of the first item
    mid_point = first_item.rectangle().mid_point()

    # Hover over the first item using pyautogui
    pyautogui.moveTo(mid_point.x, mid_point.y)


def main():
    # Launch JoyToKey
    launch_application(CONTENT_MANAGER_PATH)
    time.sleep(SLEEP_DURATION)  # Wait for the application to load

    # Connect to the application
    main_window = connect_to_application(CONTENT_MANAGER_PATH)
    time.sleep(SLEEP_DURATION)  # Wait for the connection to establish

    # Set focus on the main window
    focus_on_window(main_window)

    main_window.set_focus()

    # Open Assetto Corsa Settings
    keyboard.send('alt+f2') # This sends the minimize keystrokes to the active window
    time.sleep(3)

    # Identify the "AUDIO" button and click it
    audio_button = main_window.child_window(title="AUDIO", control_type="Text")
    audio_button.click_input()


    # Click Audio Drop Down Button
    ac_audio_menu_item = main_window.child_window(auto_id="PART_Menu", control_type="Menu")
    
    # Hover over the first item in the dropdown to make the other items visible
    hover_over_first_item(ac_audio_menu_item)
    
    # Now the button should be visible, get the button via the "Static" control with the title "HQ-GripV3"
    ac_audio_menu_button = ac_audio_menu_item.child_window(title="VR-V1", control_type="Text")
    # Click the button
    ac_audio_menu_button.click_input()
    time.sleep(1)


    # Open Assetto Corsa Settings
    keyboard.send('alt+f2') # This sends the minimize keystrokes to the active window
    time.sleep(3)

    # Identify the "AUDIO" button and click it
    audio_button = main_window.child_window(title="VIDEO", control_type="Text")
    audio_button.click_input()


    # Click Video Drop Down Button
    ac_video_menu_item = main_window.child_window(auto_id="PART_Menu", control_type="Menu")
    
    # Hover over the first item in the dropdown to make the other items visible
    hover_over_first_item(ac_video_menu_item)
    
    # Now the button should be visible, get the button via the "Static" control with the title "HQ-GripV3"
    ac_video_menu_button = ac_video_menu_item.child_window(title="HQ-HDR", control_type="Text")
    # Click the button
    ac_video_menu_button.click_input()
    time.sleep(1)


    # Open Content Manager Settings 
    keyboard.send('alt+f3') # This sends the minimize keystrokes to the active window
    
    #main_window.print_control_identifiers()
    cm_menu_item = main_window.child_window(auto_id="PART_Menu", control_type="Menu")
    #cm_menu_item.click_input()
    # Hover over the first item in the dropdown to make the other items visible
    hover_over_first_item(cm_menu_item)
    
    # Now the button should be visible, get the button via the "Static" control with the title "HQ-GripV3"
    hq_button = cm_menu_item.child_window(title="HQ-GripV3", control_type="Text")
    # Click the button
    hq_button.click_input()
    


    
    time.sleep(3)


    # Minimize the window
    #main_window.minimize()
    #print("Window minimized")

if __name__ == "__main__":
    main()
