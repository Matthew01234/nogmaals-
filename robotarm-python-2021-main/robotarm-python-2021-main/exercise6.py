from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:

for i in range(0,7,1):
 i * robotArm.moveRight()

for i in range (0,8,1):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.moveLeft()  

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()