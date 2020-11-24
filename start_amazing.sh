#!/bin/bash

# Update repo
git -C /home/pi/AmazingPi pull

# Install requirements
#pip install -r /home/pi/AmazingPi/requirements.txt

# Run Amazing app
python /home/pi/AmazingPi/amazing.py >> /home/pi/AmazingPi.log 2>&1
