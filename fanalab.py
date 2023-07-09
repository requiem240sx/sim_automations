import argparse
import time
import subprocess
from pywinauto import Application

FANALAB_EXE = r"C:\Program Files (x86)\Fanatec\FanaLab\Control\FanaLab.exe"


def get_game_name_arg():
    """Parse command line argument for game name."""
    parser = argparse.ArgumentParser(description="Script to find a game profile in FanaLab.")
    parser.add_argument("game_name", help="The name of the game profile to find.")
    args = parser.parse_args()
    return args.game_name


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

def main():

    game_name_arg = get_game_name_arg()  # Get game name from command line argument
    
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
        #print("Selected game item:")
        #print(f"Item window text: {item.window_text()}")
        #print(f"Item class: {item.class_name()}")
        #print(f"Item properties: {item.element_info}")
        #print("Child items:")

        # Get the game name from the 'Currently Modifying Game Profile:' TextBlock
        game_name = get_game_name(main_window)

        # Skip the game profile if the name is '(Work in Progress)'
        if game_name == '(Work in Progress)':
            continue

        if game_name is not None:
            if game_name == game_name_arg:
                print(f"Game match found: {game_name}")
                print(f"Checking Profiles for: {game_name}")
                #  Need to move this game portion to a function, then add another function for checking a games profiles. 

            else:
                print(f"Not a Game Match: {game_name}")


if __name__ == "__main__":
    main()
