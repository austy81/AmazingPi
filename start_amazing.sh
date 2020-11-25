#!/bin/bash

# Update repo
cd /home/pi/AmazingPi && git reset --hard && git pull

# Install requirements
#pip install -r /home/pi/AmazingPi/requirements.txt

# Run Amazing app
python /home/pi/AmazingPi/amazing.py >> /home/pi/AmazingPi.log 2>&1
