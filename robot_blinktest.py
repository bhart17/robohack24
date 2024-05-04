from sbot import Robot
from sbot import GPIOPinMode
import time

robot = Robot()

my_arduino = robot.arduino

my_arduino.pins[13].mode = GPIOPinMode.OUTPUT

while True:

    my_arduino.pins[13].digital_value = True

    time.sleep(1)

    my_arduino.pins[13].digital_value = False

    time.sleep(1)





