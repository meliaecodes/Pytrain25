from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Declare standard MicroPython modules
from usys import stdin, stdout
from uselect import poll

# Initialise the lego components
hub = CityHub()
train = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B)

# Register stdin for polling to allow you to wait for incoming data without blocking. 
keyboard = poll()
keyboard.register(stdin)

def victory_lap(station_color):
    # give the train some time to leave the station
    wait(300)
    while True:
        color = sensor.color()
        if color == station_color:
            train.stop()
            break
        wait(20)

while True:

    # Read a byte
    cmd = stdin.buffer.read(1)
    print(cmd)

    # Decide what to do based on the command
    if cmd == b"l":
        train.dc(50)
        victory_lap(Color.WHITE)
    elif cmd == b"a":
        # accelerate
        train.dc(50)
    elif cmd == b"r":
        # reverse
        train.dc(-50)
    elif cmd == b"s":
        train.stop()
    elif cmd == b"b":
        break
    
    stdout.buffer.write(b"OK")