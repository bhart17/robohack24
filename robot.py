from sbot import Robot
import time
import RPi.GPIO as gpio

robot = Robot()

motors = robot.motor_board.motors
servos = robot.servo_board.servos

#servos
claw_l = servos[0]
claw_r = servos[1]
lift_l = servos[2]
lift_r = servos[3]

# pins
can = 20

# setup gpio
gpio.setmode(gpio.BCM)
gpio.setup(can, gpio.IN)
gpio.setup(16, gpio.OUT)
gpio.output(16, 1)


def stop():
    motors[0].power = 0
    motors[1].power = 0

def drive(power, duration):
    motors[0].power = power * 0.96
    motors[1].power = -power
    robot.sleep(duration)
    stop()

def turn(power, duration):
    motors[0].power = power
    motors[1].power = power
    robot.sleep(duration)
    stop()

def claw_open():
    # open
    claw_l.position = -0.2
    claw_r.position = 0.2

def claw_half_open():
    claw_l.position = 0.2
    claw_r.position = -0.2

def claw_close():
    # close
    claw_l.position = 1
    claw_r.position = -1

def claw_up():
    # up
    lift_l.position = 0.8
    lift_r.position = -0.8

def claw_down():
    # down
    lift_l.position = -1
    lift_r.position = 1

claw_down()
claw_open()
#drive around 2m
drive(0.4, 3.7)
#pick up a can
if (gpio.input(can) == 1):
    claw_close()
    robot.sleep(1)
    claw_up()
    robot.sleep(2)
    claw_half_open()
    robot.sleep(2)
    claw_down()
    robot.sleep(1)
    claw_open()
#turn left a bit
turn(0.2, 0.8)
#drive again
drive(0.4, 2)
    
