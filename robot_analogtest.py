from sbot import Robot
from sbot import GPIOPinMode
from sbot import AnalogPins
import time

robot = Robot()

my_arduino = robot.arduino

my_arduino.pins[AnalogPins.A0].mode = GPIOPinMode.INPUT



while True:

    print(my_arduino.pins[AnalogPins.A0].analog_value)
    
    time.sleep(0.001)
    





