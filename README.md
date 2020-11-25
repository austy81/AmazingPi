![AmazingPi](logo.jpg?raw=true "AmazingPi")

This is our ESPRG present to Allan, the best manager that Microsoft office in Prague has ever seen.

This project serves as a proof of Allan's bestness - he managed to create such a great team that they not just bought some random goodbye booze for him but gathered to create this hardware present - online, in the times of coronavirus. Ain't this amazing?

# Clone repository
Into Raspberry Pi home by running following commands.
```
cd /home/pi
git clone --depth 1 https://github.com/austy81/AmazingPi.git
```

# Make sh file executable
```
chmod +x /home/pi/AmazingPi/start_amazing.sh
```

# Run Amazing application on Raspberry startup
```
sudo crontab -e
@reboot /home/pi/AmazingPi/start_amazing.sh
```