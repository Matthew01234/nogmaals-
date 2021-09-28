from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range (0,4):
    for x in range(0,1+i):
        robotArm.grab()
        for y in range (0,6):
                robotArm.moveRight()
        robotArm.drop()
        for z in range(0,6):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()