from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

robotArm.speed = 2
for i in range (20):
    robotArm.grab()
    robotArm.scan()
    color = robotArm.scan()
    if color == 'red':
        for i in range (9):
            robotArm.moveRight()
            
        robotArm.drop()
        for i in range (9):
            robotArm.moveLeft()

    else:
         robotArm.drop()
         robotArm.moveRight()

  
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

