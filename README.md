![AmazingPi](logo.jpg?raw=true "AmazingPi")

This is our ESPRG present to Allan, the best manager that Microsoft office in Prague has ever seen.

This project serves as a proof of Allan's bestness - he managed to create such a great team that they not just bought some random goodbye booze for him but gathered to create this hardware present - online, in the times of coronavirus. Ain't this amazing?

We prepared for you something to remember us and made it open source, so everyone can use it!

# Project 
Use Raspberry Pi as machine which plays on button press one random file from samples/questions directory and random samples/answer. Belive me, its fun.
You just need to connect button between [GPIO 2 (pin 2) and any ground pin](https://www.raspberrypi.org/documentation/usage/gpio/).
And for sure you need to connect repro to 3.5mm jack. Without that, you won't hear it :)

## Clone repository
Into Raspberry Pi home by running following commands.
```
cd /home/pi && git clone https://github.com/austy81/AmazingPi.git
```

## Start it after boot
```
sudo systemctl edit --force --full amazingPi.service
```

Enter in following content:

```
[Unit]
Description=AmazingPi Service
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi
ExecStart=sh /home/pi/AmazingPi/start.sh

[Install]
WantedBy=multi-user.target
```

And run following commands to start service:

```
systemctl status amazingPi.service
sudo systemctl enable amazingPi.service
sudo systemctl start amazingPi.service
```

## You can edit the unit-file and show it. After editing you must restart the service to take effect.
```
sudo systemctl edit --full amazingPi.service
sudo systemctl restart amazingPi.service
```

## Wait for network
Raspberian does not wait for network connection during boot sequence, as a result GIT Pull fails.

To fix it raspi-config change is needed:
```
sudo raspi-config
```
Select option
- '4 Wait for network at boot'
    - Slow Wait for network connection before completing boot
- confirm OK

## Update repo manually
To update code to latest version in Raspberry run:
```
cd /home/pi/AmazingPi && git reset --hard && git pull
```

## Alternatively use crontab to shcedule
```
sudo crontab -e
@reboot sh /home/pi/AmazingPi/start.sh
```
