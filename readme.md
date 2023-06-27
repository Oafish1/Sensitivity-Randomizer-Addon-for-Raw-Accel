# Sensitivity Randomizer Addon for a1xd Raw Accel
Very barebones sensitivity randomizer addon for [Raw Accel](https://github.com/a1xd/rawaccel) by [a1xd](https://github.com/a1xd).

## Use Case
Certain games and services such as Valorant and FaceIt do not work well with the Interception mouse driver.  As such, programs such as [Whisperrr's](https://github.com/Whisperrr/SensitivityRandomizer) and [Dardonkov's](https://github.com/dardonkov/Random-Sens) cannot be used.  However, the driver Raw Accel uses is signed and has safeguards to prevent abuse, and is thereby allowed in more anticheats.

## Functionality
Uniformly samples between `MIN_SENSITIVITY` and `MAX_SENSITIVITY` every `STEP_TIME` seconds and applies a new sensitivity.  These values can be modified at the top of the `randomize_raw_accel.py` file.  The functionality is very barebones, and is only meant as an interim solution while other programs are developed.

Please exit the program using CTRL+C, as otherwise the sensitivity will remain changed.  Also please back-up your `settings.json` file, as the program modifies this to change your sensitivity.

## Installation
First, install a version of [Python 3](https://www.python.org/downloads/).  Paste all files in the Raw Accel Directory (where `settings.json` and `writer.exe` are located).  Modify the values in `randomize_raw_accel.py` as desired and click `randomize_raw_accel.bat` to run.
