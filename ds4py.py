import pygame

##this code was just adapted from the standard example on the pygame joystick page, TODO:REMOVE TEXTPRINT PYGAME STUFF AND ADD ANALOGUES
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()
    
# Get ready to print
textPrint = TextPrint()

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
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
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
        #if event.type == pygame.JOYAXISMOTION:
        #   print("Joyaxis button.")
        if event.type == pygame.JOYHATMOTION:
            #print("Joyhat button.")
            DPAD = joystick.get_hat(0)
            if(DPAD == (0,1)):
                print("UP pressed")
            if(DPAD == (0,-1)):
                print("DOWN pressed")
            if(DPAD == (-1,0)):
                print("LEFT pressed")
            if(DPAD == (1,0)):
                print("RIGHT pressed")


    # DRAWING STEP
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # # Get count of joysticks
    # joystick_count = pygame.joystick.get_count()

    # textPrint.printt(screen, "Number of joysticks: {}".format(joystick_count) )
    # textPrint.indent()
    
    # # For each joystick:
    # for i in range(joystick_count):
    #     joystick = pygame.joystick.Joystick(i)
    #     joystick.init()
    
    #     # Get the name from the OS for the controller/joystick
    #     name = joystick.get_name()
    #     textPrint.printt(screen, "Joystick name: {}".format(name) )
        
    #     # Usually axis run in pairs, up/down for one, and left/right for
    #     # the other.
    #     axes = joystick.get_numaxes()
    #     textPrint.printt(screen, "Number of axes: {}".format(axes) )
    #     textPrint.indent()
        
    #     for i in range( axes ):
    #         axis = joystick.get_axis( i )
    #         textPrint.printt(screen, "Axis {} value: {:>6.3f}".format(i, axis) )
    #     textPrint.unindent()
            
    #     buttons = joystick.get_numbuttons()
    #     textPrint.printt(screen, "Number of buttons: {}".format(buttons) )
    #     textPrint.indent()

    #     for i in range( buttons ):
    #         button = joystick.get_button( i )
    #         textPrint.printt(screen, "Button {:>2} value: {}".format(i,button) )
    #     textPrint.unindent()
            
    #     # Hat switch. All or nothing for direction, not like joysticks.
    #     # Value comes back in an array.
    #     hats = joystick.get_numhats()
    #     textPrint.printt(screen, "Number of hats: {}".format(hats) )
    #     textPrint.indent()

    #     for i in range( hats ):
    #         hat = joystick.get_hat( i )
    #        # print("Hat {} value: {}".format(i, str(hat)) )
    #     textPrint.unindent()
        
    #     textPrint.unindent()

    
    # # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    
    # # Go ahead and update the screen with what we've drawn.
    # pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(20)
    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()