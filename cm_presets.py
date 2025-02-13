import subprocess
import time
import argparse
import pyautogui
from pywinauto import Application
import keyboard

# Define constants
CONTENT_MANAGER_PATH = r"C:\Users\dominic\Documents\ac_mods\Content Manager.exe"

def get_args():
    parser = argparse.ArgumentParser(description="Command line argument parser")
    parser.add_argument("--ac_audio_preset", type=str, required=True, help="Name of the preset to select from AC Audio settings")
    parser.add_argument("--ac_video_preset", type=str, required=True, help="Name of the preset to select from AC Video settings")
    parser.add_argument("--ac_controls_preset", type=str, required=True, help="Name of the preset to select from AC Controls settings")
    parser.add_argument("--cm_preset", type=str, required=True, help="Name of the preset to select from CM settings")
    args = parser.parse_args()
    return args.ac_audio_preset, args.ac_video_preset, args.ac_controls_preset, args.cm_preset

def launch_application(app_path):
    try:
        subprocess.Popen([app_path])
        print(f"Content Manager - Successfully launched {app_path}")
    except Exception as e:
        print(f"Content Manager - Failed to launch {app_path}: {e}")

def connect_to_application(app_path):
    try:
        app = Application(backend="uia").connect(path=app_path)
        main_window = app.window()
        print(f"Content Manager - Successfully connected to {app_path}")
        return main_window
    except Exception as e:
        print(f"Content Manager - Failed to connect to {app_path}: {e}")

def focus_on_window(window):
    try:
        window.set_focus()
        print("Content Manager - Window focus set")
    except Exception as e:
        print(f"Content Manager - Failed to set focus: {e}")

def hover_over_first_item(menu):
    menu.click_input()
    time.sleep(.3)
    first_item = menu.children()[0]
    mid_point = first_item.rectangle().mid_point()
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
    try:
        target_item = menu_item.child_window(title=item_name, control_type="Text")
        target_item.click_input()
        print(f"Successfully selected: {item_name}")
        time.sleep(.5)
    except Exception as e:
        print(f"ERROR: Preset '{item_name}' not found in menu '{menu_id}'. Available options should be verified.")
    target_item.click_input()
    time.sleep(.5)

def main():
    ac_audio_preset, ac_video_preset, ac_controls_preset, cm_preset = get_args()
    launch_application(CONTENT_MANAGER_PATH)
    time.sleep(3)
    main_window = connect_to_application(CONTENT_MANAGER_PATH)
    time.sleep(1)
    focus_on_window(main_window)
    main_window.set_focus()
    handle_menu_selection(main_window, 'alt+f2', "AUDIO", "PART_Menu", ac_audio_preset)
    handle_menu_selection(main_window, 'alt+f2', "VIDEO", "PART_Menu", ac_video_preset)
    handle_menu_selection(main_window, 'alt+f2', "CONTROLS", "PART_Menu", ac_controls_preset)
    handle_menu_selection(main_window, 'alt+f3', None, "PART_Menu", cm_preset)

if __name__ == "__main__":
    main()
