import atexit
import json
import random
import subprocess
import time

RAW_ACCEL_FOLDER = './'
MAX_SENSITIVITY = 2
MIN_SENSITIVITY = .5
STEP_TIME = 10

# Read existing JSON
with open(RAW_ACCEL_FOLDER + 'settings.json', 'r') as f:
    data = json.load(f)
    
# Write handling
def write_sensitivity(sensitivity=1):
    # Write 'settings.json'
    data['profiles'][0]['Sensitivity multiplier'] = sensitivity
    with open(RAW_ACCEL_FOLDER + 'settings.json', 'w') as f:
        json.dump(data, f)
    # Call Raw Accel writer
    subprocess.call([RAW_ACCEL_FOLDER + 'writer', RAW_ACCEL_FOLDER + 'settings.json'])

# Reset sensitivity on exit
atexit.register(write_sensitivity)

# Loop forever
while True:
    # Generate new sensitivity
    new_sensitivity = random.uniform(MIN_SENSITIVITY, MAX_SENSITIVITY)
    print(new_sensitivity)
    # Apply new sensitivity
    write_sensitivity(new_sensitivity)
    # Wait for next randomization
    time.sleep(STEP_TIME)
