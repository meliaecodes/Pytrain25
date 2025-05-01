from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = CityHub()


# Standard MicroPython modules
from usys import stdin, stdout
from uselect import poll

motor = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B)


# Optional: Register stdin for polling. This allows
# you to wait for incoming data without blocking.
keyboard = poll()
keyboard.register(stdin)

def victory_lap(station_color):
    # give the train some time to leave the station
    motor.dc(50)
    wait(300)
    while True:
        color = sensor.color()
        if color == station_color:
            motor.stop()
            break
        wait(20)

while True:

    # Let the remote program know we are ready for a command.
    stdout.buffer.write(b"rdy")

    # Optional: Check available input.
    while not keyboard.poll(0):
        # Optional: Do something here.
        wait(10)

    # Read three bytes.
    cmd = stdin.buffer.read(3)

    # Decide what to do based on the command.
    if cmd == b"fwd":
        motor.dc(50)
    elif cmd == b"lap":
        victory_lap(Color.WHITE)
    elif cmd == b"rev":
        motor.dc(-50)
    elif cmd == b"stp":
        motor.stop()
    elif cmd == b"bye":
        break