# P1 Smart Meter reader

=============================================

### Description
I have combined much information from the web to construct my
personal P1 Smart Meter reader. This reader continuously reads from the
P1 meter and sends the data to a Postgresql server hosted on another Raspberry Pi
at home.

### Setup Raspberry Zero W
Install a desired version of Raspberry with [Raspberry Pi imager](https://www.raspberrypi.com/software/). I have installed Raspberry Pi OS (Legacy 32-bit) Lite.

After that install psychopg2, to make sure you have all teh necessary binaries`;
```
sudo apt install python3-psycopg2
```

### Run the application on the Raspberry Pi Zero
A method to run a program on your Raspberry Pi at startup is to use the systemd files. systemd provides a standard process for controlling what programs run when a Linux system boots up. Note that systemd is available only from the Jessie versions of Raspbian OS.

#### **Step 1– Create A Unit File**

Open a sample unit file using the command as shown below:

sudo nano /lib/systemd/system/p1reader.service
Add in the following text :
```
 [Unit]
 Description=p1reader Service
 After=multi-user.target

 [Service]
 Type=idle
 ExecStart=/usr/bin/python /home/pi/projects/p1reader/main.py

 [Install]
 WantedBy=multi-user.target
```

This defines a new service called “Sample Service” and we are requesting that it is launched once the multi-user environment is available. The “ExecStart” parameter is used to specify the command we want to run. The “Type” is set to “idle” to ensure that the ExecStart command is run only when everything else has loaded. Note that the paths are absolute and define the complete location of Python as well as the location of our Python script.

In order to store the script’s text output in a log file you can change the ExecStart line to:

```
ExecStart=/usr/bin/python /home/pi/sample.py > /home/pi/sample.log 2>&1
```

The permission on the unit file needs to be set to 644 :

```
sudo chmod 644 /lib/systemd/system/p1reader.service
```

#### **Step 2 – Configure systemd**

Now the unit file has been defined we can tell systemd to start it during the boot sequence :
```
sudo systemctl daemon-reload
sudo systemctl enable p1reader.service
```
Reboot the Pi and your custom service should run:
```
sudo reboot
```

### Credits
Credits for the electronics go to:

**Jan ten Hove:**
* https://github.com/jantenhove
* http://domoticx.com/p1-poort-slimme-meter-uitlezen-hardware/


Credits for the initial code go to:

**Jan van Haarst:**
* https://github.com/jvhaarst

_Author: Michèl Borgman_