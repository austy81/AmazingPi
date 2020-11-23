![AmazingPi](logo.jpg?raw=true "AmazingPi")

This is our ESPRG present to Allan, the best manager that Microsoft office in Prague has ever seen. 

This project serves as a proof of Allan's bestness - he managed to create such a great team that they not just bought some random goodbye booze for him but gathered to create this hardware present - online, in the times of coronavirus. Ain't this amazing?


# How to schedule to run Amazing application on startup?

```
sudo crontab -e 
@reboot python /home/pi/AmazingPi/amazing.py >> /home/pi/AmazingPi.log 2>&1
```