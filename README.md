# Lego City Train connected to Jira using Forge and Pybricks

## Before you begin

Head over to [Forge Quest](https://developer.atlassian.com/platform/tool/forge-quest/forge-novice/preparing/?utm_campaign=dx_external_conference&utm_source=qrcode&utm_content=forgetrain_devoxxuk) to get your forge dev environment set up. It'll only take a moment - and if you don't have a Lego train, why not check out one of the other fun tutorials. 

## You will need

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
* Forge developer environment

## Quick start guide

1. [Install pybricks on your Lego City hub](https://pybricks.com/install/) - make a note of your hubs name, we'll use that later! Don't worry, you can also use pybricks to put the original lego firmware back at any time!
1. Use https://code.pybricks.com/ to store the `celebrationTrain.py` python routine in the `hub` directory on your Lego city hub flash memory See [pybricks docs](https://pybricks.com/install/technic-boost-city/#saving-a-program-on-the-hub)
1. Change to the `uvicorn` directory and run ```uvicorn pytrainapi:app --reload``` and follow the directions to connect your lego city hub. 
1. In a new terminal window run ```ngrok http 8000```
1. Open the [Forge pytrain_trigger project README](/Forge/pytrain_trigger/README.md) and follow the quick start instructions to install the forge app to your developer environment. 

### Troubleshooting

If you're using a color sensor, depending on the color of your surface you might experience difficulties with your train stopping at the right spot. My desk is wood laminate so white was the only colour that didn't get mistaken. 

### Additional Resources

I found this page extremely helpful in getting my API working
https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-communication/