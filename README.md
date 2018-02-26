# Cheerlights using Python and Pimoroni's Mood light

This is my take using Python and Pimoroni's Mood light kit

The main difference is there's transitions from one colour to another
instead of just put the new color there

## Installing
If using the Pimoroni's Unicorn PHAT HD, the libraries are needed


    sudo apt-get install python-unicornhathd python3-unicornhathd


## Running

If using Piromoroni's kit, sudo is necessary:

    **sudo python cheerlights.py**

## About
Cheerlights is a colaborative IoT project. Everytime someone changes the color, every device around the world 
(and outside too) connected to Cheerlights API will display the same color.

More info on: http://cheerlights.com/

Pimoroni's Mood Light:
https://shop.pimoroni.com/collections/kits/products/mood-light-pi-zero-w-project-kit

Pimoroni's Unicorn PHAT HD github page
https://github.com/pimoroni/unicorn-hat


## Run automatically on Raspberry PI start 

Just added to cron

    sudo crontab -e
    @reboot /usr/bin/python /home/pi/cheerlights/cheerlights.py &


