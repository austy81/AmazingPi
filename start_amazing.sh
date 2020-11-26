#!/bin/bash

if [ -f /home/pi/AmazingPi/amazing.py ]
then
    echo 'amazing.py already exists.'
else
    echo 'amazing.py does not exists'
    rm -rf /home/pi/AmazingPi
    cd /home/pi && git clone https://github.com/austy81/AmazingPi.git
fi

cd /home/pi/AmazingPi && git reset --hard && git pull || echo 'Error updating repo.'

echo 'Running amazing.py'
python /home/pi/AmazingPi/amazing.py