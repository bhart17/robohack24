from sbot import Robot
from sbot import GPIOPinMode
from sbot import AnalogPins
import time

robot = Robot()

motors = robot.motor_board.motors

my_arduino = robot.arduino

# Motors and constants
lmotor = motors[1]
rmotor = motors[0]
left_scalar = -1
right_scalar = 1
motor_slow = 0.05
motor_norm = 0.2
motor_fast = 0.3

#high on white low on black

#left line following sensor
rightSensor = AnalogPins.A0
#right line following sensor
leftSensor = AnalogPins.A1

my_arduino.pins[rightSensor].mode = GPIOPinMode.INPUT
my_arduino.pins[leftSensor].mode = GPIOPinMode.INPUT

threshold = 0.1

state = (0,0) # States are defines as (0,1) where L and R = {0,1} for {black,white}
last_turn = 0 # 0 = L, 1 = R

while True:
    left_reading = my_arduino.pins[leftSensor].analog_value
    right_reading = my_arduino.pins[rightSensor].analog_value / 10
    
    print("Left:", left_reading)
    print("Right:", right_reading)
    
    l = left_reading > threshold
    r = right_reading > threshold
    
    if(not l and not r):
        # go straight
        lmotor.power = left_scalar * motor_fast
        rmotor.power = right_scalar * motor_fast
    elif(l and not r):
        # turn right
        lmotor.power = left_scalar * motor_fast
        rmotor.power = right_scalar * motor_norm
        last_turn = 1
    elif(not l and r):
        # turn left
        lmotor.power = left_scalar * motor_norm
        rmotor.power = right_scalar * motor_fast
        last_turn = 0
    else:
        # turn aggressively
        if(last_turn == 1):
            # turn right aggressive
            lmotor.power = left_scalar * motor_fast
            rmotor.power = right_scalar * motor_slow
            last_turn = 1
        else:
            # turn left aggressive
            lmotor.power = left_scalar * motor_norm
            rmotor.power = right_scalar * motor_fast
            last_turn = 0
    
    #time.sleep(0.001)
