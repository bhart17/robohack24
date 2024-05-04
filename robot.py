from sbot import Robot
from sbot import GPIOPinMode
from sbot import AnalogPins
import time

robot = Robot()

my_arduino = robot.arduino

#high on white low on black

#left line following sensor
A0 = AnalogPins.A0
#right line following sensor
A1 = AnalogPins.A1

my_arduino.pins[A0].mode = GPIOPinMode.INPUT
my_arduino.pins[A1].mode = GPIOPinMode.INPUT

threshold = 0.15

while True:
    left_reading = my_arduino.pins[A0].analog_value
    right_reading = my_arduino.pins[A1].analog_value
    print("Left:")
    print(left_reading)
    print("Right:")
    print(right_reading)

    if (left > threshold):
        #turn right a bit
    else if (right > threshold):
        #turn left a bit
    else:
        #keep going straight
    
    time.sleep(0.001)
    





