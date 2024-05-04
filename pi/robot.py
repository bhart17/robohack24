from sbot import Robot

robot = Robot()

motors = robot.motor_board.motors

def drive(power, duration):
    motors[0].power = power
    motors[1].power = -power
    robot.sleep(duration)

def turn(power, duration):
    motors[0].power = power
    motors[1].power = power
    robot.sleep(duration)

def stop():
    motors[0].power = 0
    motors[1].power = 0


while True:
    markers = robot.camera.see()
    if len(markers) > 0:
        if markers[0].azimuth > 0.1:
            turn(-0.1, 0.01)
        elif markers[0].azimuth < -0.1:
            turn(0.1, 0.01)
    else:
        stop()
        robot.sleep(0.01)
        # if markers[0].distance > 0.5:
        #     drive(0.4, 0.1)
        # elif markers[0].distance < 0.5:
        #     drive(-0.4, 0.1)