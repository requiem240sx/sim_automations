import argparse
import time
import subprocess
from pywinauto import Application
import pywinauto.timings
import keyboard

FANALAB_EXE = r"C:\Program Files (x86)\Fanatec\FanaLab\Control\FanaLab.exe"


def get_game_name_arg():
    """Parse command line argument for game name."""
    parser = argparse.ArgumentParser(description="Script to find a game profile in FanaLab.")
    parser.add_argument("game_name", help="The name of the game profile to find.")
    parser.add_argument("game_profile", help="The game profile to select.")
    args = parser.parse_args()
    return args.game_name, args.game_profile

def check_application_running(app_path):
    """Check if application is already running"""
    try:
        app = Application(backend="uia").connect(path=app_path)
        print(f"Application already running, connected to {app_path}")
        return app
    except Exception as e:
        print(f"Application not running: {e}")
        return None

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

def get_game_name(app):
    for child in app.descendants():
        if child.class_name() == 'TextBlock':
            if 'Currently Modifying Game Profile:' in child.window_text():
                game_name = child.window_text().replace('Currently Modifying Game Profile: ', '').strip()
                return game_name
    return None  # If the game name wasn't found

#def wait_for_user_confirmation(main_window, popup_name):
#    """Waits until the user closes a pop-up window with the specified name."""
#    try:
#        main_window.window(name=popup_name).wait('exists', timeout=2)  # Check if the pop-up is shown
#    except pywinauto.findwindows.ElementNotFoundError:
#        # The pop-up could not be found, which means it was not shown
#        return False  # No confirmation was needed
#    else:
#        # The pop-up was found, wait for it to be closed
#        try:
#            main_window.window(name=popup_name).wait_not('exists', timeout=pywinauto.timings.Timings.window_find_timeout)
#            return True  # Confirmation was needed and has been handled
#        except pywinauto.timings.TimeoutError:
#            # The pop-up was not closed within the timeout, the user likely denied the action
#            return None  # The user didn't confirm the action




def main():

    game_name_arg, game_profile_arg = get_game_name_arg()  # Get game name and profile from command line arguments

    # Check if the application is already running
    app = check_application_running(FANALAB_EXE)

    # If the application is not running, launch it
    if app is None:
        launch_application(FANALAB_EXE)
        time.sleep(10)   # Wait for the application to load

    # Connect to the application
    main_window = connect_to_application(FANALAB_EXE)

    # Set focus on the main window
    focus_on_window(main_window)

    # Select the 'Game Profile' tab
    game_profile_tab = main_window.child_window(title="Game Profile", control_type="TabItem")

    # Click the 'Game Profile' tab
    game_profile_tab.click_input()
    time.sleep(1) 
    
    game_list = game_profile_tab.child_window(class_name="ListBox", found_index=0)

    game_items = game_list.children(control_type="ListItem")

    for item in game_items:

        # Skip the item if it doesn't have any child fields (this skips "hidden" games in fanalab)
        if not item.children():
            continue

        item.select()  # Select the item
        time.sleep(1)  # Wait for the selection to take effect and for the new info to become visible

        # Get the game name from the 'Currently Modifying Game Profile:' TextBlock
        game_name = get_game_name(main_window)

        # Skip the game profile if the name is '(Work in Progress)'
        if game_name == '(Work in Progress)':
            continue

        if game_name is not None:
            if game_name == game_name_arg:
                print(f"Game match found: {game_name}")

                # If the game name matches, try to find and double-click the game profile
                try:
                    profile_item = main_window.child_window(title=game_profile_arg, control_type="Text")
                    profile_item.double_click_input()
                    print(f"Game profile '{game_profile_arg}' found and double-clicked.")

                    # Wait for user confirmation if a pop-up appears.
                    #confirmation_result = wait_for_user_confirmation(main_window, "Device mismatch")
                    #if confirmation_result is None:
                    #    print("User denied the action. Leaving window open.")
                    #    break
                    #elif confirmation_result:
                    #    keyboard.send('alt+space, n') # This sends the minimize keystrokes to the active window
                    #    print("Window minimized.")
                    #    break

                except Exception as e:
                    print(f"Failed to find and double-click game profile '{game_profile_arg}': {e}")

                # Minimize the window
                time.sleep(1)
                main_window.set_focus()
                keyboard.send('enter')
                keyboard.send('alt+space, n') # This sends the minimize keystrokes to the active window
                print("Window minimized.")
                break  # End the loop because we've found the game

            else:
                print(f"Currently modifying game profile: {game_name}")


if __name__ == "__main__":
    main()
