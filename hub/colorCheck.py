from pybricks.hubs import CityHub
from pybricks.pupdevices import DCMotor, Light, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = CityHub()

print(hub.battery.current())
print(hub.battery.voltage())

sensor = ColorDistanceSensor(Port.B)
train_motor = DCMotor(Port.A)

def victory_lap(station_color):
    # give the train some time to leave the station
    wait(300)
    lap = 300
    while True:
        color = sensor.color()
        if color == station_color:
            print("stopping...")
            train_motor.stop()
            print(lap)
            break
        wait(20)
        lap += 20

def colour_test():
    red = 0
    yellow = 0
    green = 0
    white = 0
    blue = 0 
    while True:
        color = sensor.color()
        hsv = sensor.hsv()
        #print(color)
        if color == Color.RED:
            red += 1
        elif color == Color.YELLOW:
            yellow += 1
        elif color == Color.GREEN:
            green += 1
        elif color == Color.BLUE:
            blue += 1
        elif color == Color.WHITE:
            print(hsv)
            white += 1
            print("STOP")
            train_motor.stop() 
            break
        wait(50)
        print(f"red={red},yellow={yellow},white={white},blue={blue},green={green}")

train_motor.dc(50)
print("lap - stop at white")
victory_lap(Color.WHITE)


