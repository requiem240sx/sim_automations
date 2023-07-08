import time
import subprocess
from pywinauto import Application

FANALAB_EXE = r"C:\Program Files (x86)\Fanatec\FanaLab\Control\FanaLab.exe"
SLEEP_DURATION = 5

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

def main():
    # Check if the application is already running
    app = check_application_running(FANALAB_EXE)

    # If the application is not running, launch it
    if app is None:
        launch_application(FANALAB_EXE)
        time.sleep(SLEEP_DURATION)  # Wait for the application to load

    # Connect to the application
    main_window = connect_to_application(FANALAB_EXE)

    # Set focus on the main window
    focus_on_window(main_window)

    # Select the 'Game Profile' tab
    game_profile_tab = main_window.child_window(title="Game Profile", control_type="TabItem")

    # Click the 'Game Profile' tab
    game_profile_tab.click_input()
    time.sleep(SLEEP_DURATION)


    #print(main_window.print_control_identifiers())
    
    # Iterate over ListBox items
    #list_box = main_window.child_window(title="List Box", control_type="List")
    
    # This should be close... 
    game_list = game_profile_tab.child_window(class_name="ListBox", found_index=0, found_only=True, control_type="List")
    #game_list.click_input()

    #for item in game_list.children():
        # Click on the item
    #    item.click_input()

        # Wait for UI to update
    #    time.sleep(1)
    #    print("Still checking..")

        # Check if the "Dirt Rally" string appears in the window's text
    #    if "DiRT Rally 2.0" in main_window.window_text():
    #        print("Found the 'DiRT Rally 2.0' item.")
    #        break


    #print(main_window.dump_tree())
    #tab = main_window.child_window(title="Game Profile", control_type="Tab")
    #tab.click()


if __name__ == "__main__":
    main()
