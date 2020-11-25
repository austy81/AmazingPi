#!/bin/bash
{ 
    cd /home/pi/AmazingPi && 
    git reset --hard && 
    git pull && 
    python /home/pi/AmazingPi/amazing.py
} || python /home/pi/AmazingPi/amazing.py