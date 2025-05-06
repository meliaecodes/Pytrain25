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

def test_connection(rpt):
    # test the connection is working by making the city hub lights flash
    for x in range(rpt):
        hub.light.on(Color.VIOLET)
        wait(200)
        hub.light.off()
        wait(100)
        hub.light.on(Color.GREEN)
        wait(200)
        hub.light.off()
        wait(100)
        hub.light.on(Color.MAGENTA)
        wait(200)
        hub.light.off()
        wait(100)
    hub.light.on(Color.BLUE)

def victory_lap(station_color):
    # give the train some time to leave the station
    motor.dc(50)
    wait(300)
    #note, if you don't have a sensor, you can remove the below while loop and just estimate the time to do a lap with wait
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
    elif cmd == b"tst":
        test_connection(3)
    elif cmd == b"rev":
        motor.dc(-50)
    elif cmd == b"stp":
        motor.stop()
    elif cmd == b"bye":
        break