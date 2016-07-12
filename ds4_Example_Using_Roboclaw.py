#Exercises the DS4 using Python, tested and working on Raspberry Pi 3
#Author <Samuel.walsh@manchester.ac.uk>
#Data 11/07/16

##this code was just adapted from the standard example on the pygame joystick page, TODO:ADD ANALOGUES
import pygame
import time
import roboclaw
from time import sleep

#Roboclaw stuff--------------------------------
#Windows comport name
#roboclaw.Open("COM3",115200)
#Linux comport name
roboclaw.Open("/dev/ttyACM0",115200)
address = 0x80
#Motor safe state
roboclaw.ForwardMixed(address, 0)
roboclaw.TurnRightMixed(address, 0)

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
R2_Analogue = 0
L2_Analogue = 0
Left_Analogue = (0,0)
Right_Analogue = (0,0)

enableAnalogueMode = False #if you press 'share' it will start streaming analogue data.. press it again to stop

def remap( x, oMin, oMax, nMin, nMax ):

	#range check
	if oMin == oMax:
		print "Warning: Zero input range"
		return None

	if nMin == nMax:
		print "Warning: Zero output range"
		return None

	#check reversed input range
	reverseInput = False
	oldMin = min( oMin, oMax )
	oldMax = max( oMin, oMax )
	if not oldMin == oMin:
		reverseInput = True

	#check reversed output range
	reverseOutput = False   
	newMin = min( nMin, nMax )
	newMax = max( nMin, nMax )
	if not newMin == nMin :
		reverseOutput = True

	portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
	if reverseInput:
		portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

	result = portion + newMin
	if reverseOutput:
		result = newMax - portion

	return result

def Show_Snapshot_All_Axes():
	'''When you press 'options' on the pad it will print out every analogue value to terminal'''
	axes = joystick.get_numaxes()
	Left_Analogue = (joystick.get_axis(0),joystick.get_axis(1))
	#Left_Analogue[1] = joystick.get_axis(1)
	print("Left analogue X,Y: ", Left_Analogue)
	Right_Analogue = (joystick.get_axis(2),joystick.get_axis(5))
	print("Right analogue X,Y: ", Right_Analogue)

	L2_Analogue = joystick.get_axis(3)
	print("L2 analogue value: {:>6.3f}".format(L2_Analogue))
	R2_Analogue = joystick.get_axis(4)
	print("R2 analogue value: {:>6.3f}".format(R2_Analogue))
	print("Number of axes: {}".format(axes) )
	
	for i in range(axes):
		axis = joystick.get_axis( i )
		print("Axis {} value: {:>6.3f}".format(i, axis))

def Send_R2_To_Motor(dutyCycle):
	'''This function uses a motor driver, it sends the analogue
	trigger value from R2 , it is just an example of how these values can be used'''
	print("R2 analogue value: {:>6.3f}".format(dutyCycle))
	dutyCycle = int(remap(dutyCycle,-1.0,1.0,0,127.0))
	print("R2 analogue value mapped to Robotclaw Duty Cycle: ", dutyCycle)
	if(dutyCycle > 0):
		roboclaw.ForwardM1(address,dutyCycle)
	elif(dutyCycle == 0 or -1):
		roboclaw.ForwardM1(address, 0)

# -------- Main Program Loop -----------
while True:
	# EVENT PROCESSING STEP
	for event in pygame.event.get(): # User did something
		# Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
		if event.type == pygame.JOYAXISMOTION:
			if(enableAnalogueMode == True):
				Left_Analogue = (joystick.get_axis(0),joystick.get_axis(1))
				#Left_Analogue[1] = joystick.get_axis(1)
				print("Left analogue X,Y: ", Left_Analogue)
				Right_Analogue = (joystick.get_axis(2),joystick.get_axis(5))
				print("Right analogue X,Y: ", Right_Analogue)

				L2_Analogue = joystick.get_axis(3)
				print("L2 analogue value: {:>6.3f}".format(L2_Analogue))
				R2_Analogue = joystick.get_axis(4)
				print("R2 analogue value: {:>6.3f}".format(R2_Analogue))
				Send_R2_To_Motor(R2_Analogue)

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
				'''Robo claw uses a duty cycle of 0-127 so 32,64,96,127 are a quarter step change each time'''
				print("X pressed")
				roboclaw.ForwardM1(address, 32)
			if(CIRCLE == 1):
				print("CIRCLE pressed")
				roboclaw.ForwardM1(address, 64)
			if(TRIANGLE == 1):
				print("TRIANGLE pressed")
				roboclaw.ForwardM1(address, 96)
			if(SQUARE == 1):
				print("SQUARE pressed")
				roboclaw.ForwardM1(address, 127)
			if(R1 == 1):
				print("R1 pressed")
				roboclaw.ForwardM1(address, 0)
			if(R2 == 1):
				print("R2 pressed")
			if(L1 == 1):
				print("L1 pressed")
			if(L2 == 1):
				print("L2 pressed")
			if(SHARE == 1):
				print("SHARE pressed")
				if(enableAnalogueMode == False):
					enableAnalogueMode = True
				else:
					enableAnalogueMode = False
			if(OPTIONS == 1):
				print("OPTIONS pressed")
				print("Showing a snap shot of all analogue values")
				Show_Snapshot_All_Axes()
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

   