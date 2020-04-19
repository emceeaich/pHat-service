# pHat-service
Expose a Pimoroni pHat HD as a web service for IoT

## Setup

Install the pHat HD board on your Raspberry Pi and follow the installation directions in https://github.com/pimoroni/scroll-phat-hd

Use PIP3 to install `flask` and it's dependencies

Place the `clear.py` and `server.py` files in `/home/pi/`

Enable `phathd.service` using `systemctld` (see https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

Restart your Pi. 

Confirm that you can reach `(your pi's hostname).local:5000` on a browser.

You should see the message:

> `PUT the JSON request body {"script": script} to / where script is one of plasma, life, fire, swirl, none`

Don't forget to set `Content-type: application/json` in the request headers.

To add new scripts, modify `_scripts` in the definition of the `ScriptController` class in `server.py`.