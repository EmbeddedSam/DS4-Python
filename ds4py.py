#Exercises the DS4 using Python, tested and working on Raspberry Pi 3
#Author <Samuel.walsh@manchester.ac.uk>
#Data 11/07/16

#123


##this code was just adapted from the standard example on the pygame joystick page, TODO:ADD ANALOGUES
import pygame

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

#Variables to hold buttons
X = 0
CIRCLE = 0
SQUARE = 0
TRIANGLE = 0
R2 = 0
R1 = 0
L2 = 0
L1 = 0
RIGHTSTICK = 0
LEFTSTICK = 0
OPTIONS = 0
PS = 0
TRACKPAD = 0
SHARE = 0

# -------- Main Program Loop -----------
while True:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
           # print("Joystick button pressed.")

            SQUARE = joystick.get_button(0)
            X = joystick.get_button(1)
            CIRCLE = joystick.get_button(2)
            TRIANGLE = joystick.get_button(3)
            L1 = joystick.get_button(4)
            R1 = joystick.get_button(5)
            L2 = joystick.get_button(6)
            R2 = joystick.get_button(7)   
            SHARE = joystick.get_button(8)
            OPTIONS = joystick.get_button(9)
            LEFTSTICK = joystick.get_button(10)
            RIGHTSTICK = joystick.get_button(11)
            PS = joystick.get_button(12)
            TRACKPAD = joystick.get_button(13)

            if(X == 1):
                print("X pressed")
            if(CIRCLE == 1):
                print("CIRCLE pressed")
            if(SQUARE == 1):
                print("SQUARE pressed")
            if(TRIANGLE == 1):
                print("TRIANGLE pressed")
            if(R1 == 1):
                print("R1 pressed")
            if(R2 == 1):
                print("R2 pressed")
            if(L1 == 1):
                print("L1 pressed")
            if(L2 == 1):
                print("L2 pressed")
            if(SHARE == 1):
                print("SHARE pressed")
            if(OPTIONS == 1):
                print("OPTIONS pressed")
            if(RIGHTSTICK == 1):
                print("RIGHTSTICK pressed")
            if(LEFTSTICK == 1):
                print("LEFTSTICK pressed")
            if(PS == 1):
                print("PS pressed")
            if(TRACKPAD == 1):
                print("TRACKPAD pressed")

        #if event.type == pygame.JOYBUTTONUP:
            #print("Joystick button released.")
        #if event.type == pygame.JOYAXISMOTION: THIS IS WHERE ANALOGUES ARE.. use pygame.get_axis(i)
        #   print("Joyaxis button.")
        if event.type == pygame.JOYHATMOTION:
            #print("Joyhat button.")
            DPAD = joystick.get_hat(0) #this is stored in a tuple
            if(DPAD == (0,1)):
                print("UP pressed")
            if(DPAD == (0,-1)):
                print("DOWN pressed")
            if(DPAD == (-1,0)):
                print("LEFT pressed")
            if(DPAD == (1,0)):
                print("RIGHT pressed")
    
pygame.quit ()