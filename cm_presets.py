import subprocess
import time
import argparse
import pyautogui
from pywinauto import Application
import keyboard

# Define constants
CONTENT_MANAGER_PATH = r"C:\Users\dominic\Documents\asseto_mods\Content Manager.exe"

def get_args():
    """
    Function to handle command line arguments.
    Returns:
    ac_audio_preset : name of the preset to select from the audio settings
    ac_video_preset : name of the preset to select from the video settings
    cm_preset : name of the preset to select from the CM settings
    """
    parser = argparse.ArgumentParser(description="Command line argument parser")
    parser.add_argument("--ac_audio_preset",
                        type=str,
                        required=True,
                        help="Name of the preset to select from the AC Audio settings")
    parser.add_argument("--ac_video_preset",
                        type=str,
                        required=True,
                        help="Name of the preset to select from the AC Video settings")
    parser.add_argument("--cm_preset",
                        type=str,
                        required=True,
                        help="Name of the preset to select from the CM settings")

    args = parser.parse_args()

    return args.ac_audio_preset, args.ac_video_preset, args.cm_preset

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
    time.sleep(.3)  # Let the dropdown expand

    # Now, find the first available child element
    first_item = menu.children()[0]

    # Get the mid point of the first item
    mid_point = first_item.rectangle().mid_point()

    # Hover over the first item using pyautogui
    pyautogui.moveTo(mid_point.x, mid_point.y)


def handle_menu_selection(main_window, shortcut, button_name, menu_id, item_name):
    """
    Handle menu selection given main window, shortcut, button_name, menu_id, item_name.

    Args:
    main_window : main window of the application
    shortcut : keyboard shortcut to send
    button_name : name of the button to click
    menu_id : id of the menu to click
    item_name : name of the item to select from the menu
    """
    # Send the keyboard shortcut
    keyboard.send(shortcut)
    time.sleep(1)

    # If a button_name is provided, find the button and click it
    if button_name is not None:
        button = main_window.child_window(title=button_name, control_type="Text")
        button.click_input()
        time.sleep(.5)

    # Find the menu and hover over its first item
    menu_item = main_window.child_window(auto_id=menu_id, control_type="Menu")
    hover_over_first_item(menu_item)

    # Find the item within the menu and click it
    target_item = menu_item.child_window(title=item_name, control_type="Text")
    target_item.click_input()
    time.sleep(.5)


def main():
    # Get command line arguments
    ac_audio_preset, ac_video_preset, cm_preset = get_args()

    # Launch the application
    launch_application(CONTENT_MANAGER_PATH)
    time.sleep(3)

    # Connect to the application
    main_window = connect_to_application(CONTENT_MANAGER_PATH)
    time.sleep(1)

    # Set focus on the main window
    focus_on_window(main_window)
    main_window.set_focus()

    # Handle AC settings
    handle_menu_selection(main_window, 'alt+f2', "AUDIO", "PART_Menu", ac_audio_preset)
    handle_menu_selection(main_window, 'alt+f2', "VIDEO", "PART_Menu", ac_video_preset)

    # Handle CM settings
    handle_menu_selection(main_window, 'alt+f3', None, "PART_Menu", cm_preset)


if __name__ == "__main__":
    main()
