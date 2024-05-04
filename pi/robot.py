from sbot import Robot

robot = Robot()

while True:
    robot.motor_board.motors[0].power = 0.5
    robot.motor_board.motors[1].power = 0.5
    robot.sleep(3)

    robot.motor_board.motors[0].power = 0
    robot.motor_board.motors[1].power = 0
    robot.sleep(1.4)

    robot.motor_board.motors[0].power = -0.5
    robot.motor_board.motors[1].power = -0.5
    robot.sleep(1)

    robot.motor_board.motors[0].power = 0
    robot.motor_board.motors[1].power = 0

    robot.sleep(4)
