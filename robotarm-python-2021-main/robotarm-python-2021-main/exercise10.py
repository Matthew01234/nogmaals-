from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
for i in range (0,5):
    robotArm.grab()
    for z in range(0,9-i * 2):
     robotArm.moveRight()
    
    robotArm.drop()
    for y in range(0,8-i * 2):
     robotArm.moveLeft()
  


robotArm.wait()