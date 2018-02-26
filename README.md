# Cheerlights using Python and Pimoroni's Mood light and a Raspberry PI

This is my take using Python and Pimoroni's Mood light kit with a Raspberry PI Zero W

The main difference is there's transitions from one colour to another
instead of just put the new color there

## Installing (Python2 and Python3)
### Required libraries
#### Requests - python2
	sudo apt-get install requests

#### Requests - python3
	sudo apt-get install python3-pip
	sudo pip3 install requests
    
If using the Pimoroni's Unicorn PHAT HD, the libraries are needed. You can check their github page for instructions:
https://github.com/pimoroni/unicorn-hat


## Running

If using Piromoroni's kit, sudo is necessary:

	**sudo python cheerlights.py**
	
for Python3

	**sudo python3 cheerlights.py**

## About
Cheerlights is a colaborative IoT project. Everytime someone changes the color, every device around the world 
(and outside too) connected to Cheerlights API will display the same color.

More info on: http://cheerlights.com/

Pimoroni's Mood Light:
https://shop.pimoroni.com/collections/kits/products/mood-light-pi-zero-w-project-kit




## Run automatically on Raspberry PI start 

Just added to cron

    sudo crontab -e
    @reboot /usr/bin/python /home/pi/cheerlights/cheerlights.py &


