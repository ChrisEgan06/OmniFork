# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       krizz                                                        #
# 	Created:      11/6/2024, 11:36:16 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *
#Constants

IDLE = 0
MAINDRIVE = 1
ARMUP = 2
ARMDOWN = 3
FORKUP = 4
FORKDOWN = 5

#Definitions
brain=Brain()

currentState = IDLE

ultraSonic = Sonar(brain.three_wire_port.a)
distance = ultraSonic.distance(MM)

leftLine = Line(brain.three_wire_port.a)
rightLine = Line(brain.three_wire_port.b)

controller = Controller()

leftMotor = Motor(Ports.PORT1,GearSetting.RATIO_18_1, False)
rightMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
armMotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True) 
forkMotor = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)

armMotor.set_stopping(HOLD)

#main function

def mainFunction():
    global currentState
    if (currentState == IDLE):
        leftMotor.stop()
        rightMotor.stop()
        if(controller.buttonA.pressing()):
            print("IDLE -> ARM UP")
            currentState = ARMUP
        elif(controller.buttonB.pressing()):
            print("IDLE -> ARM DOWN")
            currentState = ARMDOWN
        elif(controller.buttonX.pressing()):
            print("IDLE -> FORK UP")
            currentState = FORKUP
        elif(controller.buttonY.pressing()):
            print("IDLE -> FORK DOWN")
            currentState = FORKDOWN

    if (currentState == ARMUP):
        if(controller.buttonA.pressing()):
            armMotor.spin(FORWARD, 50)
        else:
            print("ARM UP -> IDLE")
            currentState = IDLE

    if (currentState == ARMUP):
        if(controller.buttonA.pressing()):
            armMotor.spin(FORWARD, -50)
        else:
            print("ARM DOWN -> IDLE")
            currentState = IDLE

    if (currentState == ARMUP):
        if(controller.buttonA.pressing()):
            forkMotor.spin(FORWARD, 50)
        else:
            print("FORK UP -> IDLE")
            currentState = IDLE

    if (currentState == ARMUP):
        if(controller.buttonA.pressing()):
            forkMotor.spin(FORWARD, -50)
        else:
            print("FORK DOWN -> IDLE")
            currentState = IDLE

while True:
    pass

        
