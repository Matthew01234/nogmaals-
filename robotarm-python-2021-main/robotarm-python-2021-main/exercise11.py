from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
color = robotArm.scan()

for i in range (0,11):
    robotArm.grab()
    color = robotArm.scan()
    if color == ('white'):
     robotArm.moveRight()
    robotArm.drop()
    robotArm.moveRight()




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()