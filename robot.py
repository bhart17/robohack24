from sbot import Robot
from sbot import GPIOPinMode
from sbot import AnalogPins
import time

robot = Robot()

motors = robot.motor_board.motors

my_arduino = robot.arduino

def stop():
    motors[0].power = 0
    motors[1].power = 0

def drive(power, duration):
    motors[0].power = power
    motors[1].power = -power
    robot.sleep(duration)
    stop()

def turn(power, duration):
    motors[0].power = power
    motors[1].power = power
    robot.sleep(duration)
    stop()



#high on white low on black

#left line following sensor
rightSensor = AnalogPins.A0
#right line following sensor
leftSensor = AnalogPins.A1

my_arduino.pins[rightSensor].mode = GPIOPinMode.INPUT
my_arduino.pins[leftSensor].mode = GPIOPinMode.INPUT

threshold = 0.1

while True:
    left_reading = my_arduino.pins[leftSensor].analog_value
    right_reading = my_arduino.pins[rightSensor].analog_value / 10
    
    print("Left:")
    print(left_reading)
    print("Right:")
    print(right_reading)

    if (left_reading > threshold):
        #turn right a bit
        turn(-0.1, 0.01)
    elif (right_reading > threshold):
        #turn left a bit
        turn(0.1, 0.01)
    else:
        #keep going straight
        drive(0.2, 0.3)
    
    #time.sleep(0.001)
