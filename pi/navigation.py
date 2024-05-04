from sbot import Robot
import math

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

def fixAngle(marker):
    # if the robot is at the wrong angle
    if marker.azimuth > 0.1:
        turn(-0.1, 0.01)
        return False
    elif marker.azimuth < -0.1:
        turn(0.1, 0.01)
        return False
    else:
        return True


def fixDistance(marker):
    if marker.id == 0 or marker.id == 1:
        target_distance = 0.9
    elif marker.id == 2 or marker.id == 3:
        target_distance = 0.7
    elif marker.id == 4 or marker.id == 5:
        target_distance = 0.6

    # while the robot is too far away from the markers
    if marker.distance > target_distance:
        drive(0.1, 0.01)
    else:
        return True


def rescan(marker_ref):
    marker_found = False
    while marker_found == False:
        markers = robot.camera.see()
        for m in markers:
            if m.id == marker_ref_id:
                marker_ref = m
                marker_found = True
    return marker_ref


# assuming closest markers show up first?

while True:
    markers = robot.camera.see()
    marker_ref = markers[0]
    marker_ref_id = markers[0].id
    while fixAngle(marker_ref) == False or fixDistance(marker_ref) == False:
        while fixAngle(marker_ref) == False:
            marker_ref = rescan(marker_ref)
        while fixDistance(marker_ref) == False:
            marker_ref = rescan(marker_ref)
    stop()
