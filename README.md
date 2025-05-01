Lego City Train connected to Jira / Confluence using Forge and Pybricks

To make your own forge train:

You will need

* A Lego City train. I used the Express Passenger Train 60337
* Track included with the Lego City Express Passenger Train (of purchased separately)
* Optional 
  * the Lego Powered up color sensor and bricks to connect to the underside of your train
  * a WHITE 2X6 or 4x6 PLATE or similar equivalent (it might be helpful to have other colours like RED, GREEN, YELLOW or BLUE as well, see Troubleshooting)
* A computer with Bluetooth and an internet connection
* An Atlassian Developer Account
* Python 3
* ngrok (if you're Atlassian staff, you'll need to use Atlas Tunnel CLI - https://developer.atlassian.com/platform/atlas-tunnel-cli/ NB INTERNAL ATLASSIAN USE ONLY)
* uvicorn - https://www.uvicorn.org/
* bleak - https://pypi.org/project/bleak/
* fastapi - https://pypi.org/project/fastapi/
* Forge environment

What to do

1. [Install pybricks on your Lego City hub](https://pybricks.com/install/) - make a note of your hubs name, we'll use that later! Don't worry, you can also use pybricks to put the original lego firmware back at any time!
1. Use https://code.pybricks.com/ to store one of the python routines in the hub directory on your hubs flash memory See [pybricks docs](https://pybricks.com/install/technic-boost-city/#saving-a-program-on-the-hub)
???
uvicorn pytrainapi:app --reload
ngrok http 8000

Troubleshooting

If you're using a color sensor, depending on the color of your surface you might experience difficulties with your train stopping at the right spot. My desk is wood laminate so white was the only colour that didn't get mistaken. 