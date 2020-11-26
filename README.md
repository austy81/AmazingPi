![AmazingPi](logo.jpg?raw=true "AmazingPi")

This is our ESPRG present to Allan, the best manager that Microsoft office in Prague has ever seen.

This project serves as a proof of Allan's bestness - he managed to create such a great team that they not just bought some random goodbye booze for him but gathered to create this hardware present - online, in the times of coronavirus. Ain't this amazing?

# Clone repository
Into Raspberry Pi home by running following commands.
```
cd /home/pi && git clone https://github.com/austy81/AmazingPi.git
```

# Start it after boot
```
sudo systemctl edit --force --full amazingPi.service
```

Enter in fllowing content:

```
[Unit]
Description=AmazingPi Service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi
ExecStart=sh /home/pi/AmazingPi/start_amazing.sh > /home/pi/AmazingPi.log

[Install]
WantedBy=multi-user.target
```

And run following commands to start service:

```
systemctl status amazingPi.service
sudo systemctl enable amazingPi.service
sudo systemctl start amazingPi.service
```

# Update repo manually
run
```
cd /home/pi/AmazingPi && git reset --hard && git pull
```

# Alternatively use crontab to shcedule
```
sudo crontab -e
@reboot sh /home/pi/AmazingPi/start_amazing.sh >> /home/pi/AmazingPi.log 2>&1
```