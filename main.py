import subprocess
import time

# Path to first script and its arguments
script1_path = 'joytokey.py'
script1_arguments = ['Assetto Corsa - Drift']

# Path to second script and its arguments
script2_path = 'fanatec_control_panel_preset.py'
script2_arguments = ['1']

# Path to third script and its arguments
script3_path = 'cm_presets.py'
script3_arguments = ['--ac_audio_preset', 'TV-V1', '--ac_video_preset', 'HQ-HDR', '--cm_preset', 'HQ-DriftV3']

def call_script(script_path, arguments):
    command = ['python', script_path] + arguments
    try:
        print(f"Executing command: {' '.join(command)}")
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {' '.join(command)}")
        print(f"Return code: {e.returncode}")
        print(f"Error output: {e.output.decode()}")


# Call first script
print(f"Calling script: {script1_path}")
call_script(script1_path, script1_arguments)

# Call second script
print(f"Calling script: {script2_path}")
call_script(script2_path, script2_arguments)

# Call third script
print(f"Calling script: {script3_path}")
call_script(script3_path, script3_arguments)
