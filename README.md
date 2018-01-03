# Cheerlights using Python and Pimoroni's Mood light

This is my take using Python and Pimoroni's Mood light kit

The main difference is there's transitions from one colour to another
instead of just put the new color there

## Running

If using Piromoroni's kit, sudo is necessary:

**sudo python cheerlights.py**


Cheerlights is a colaborative IoT project. Everytime some one changes the color, every device around the world 
(and then outside too) connected to Cheerlights will lit the same color.

More info on: http://cheerlights.com/

Pimoroni's Mood Light:
https://shop.pimoroni.com/collections/kits/products/mood-light-pi-zero-w-project-kit


## Run automatically on Raspberry PI start 

Just added to cron

    sudo crontab -e
    @reboot /usr/bin/python /home/pi/cheerlights/cheerlights.py &


