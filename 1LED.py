import RPi.GPIO as GPIO
GPIO.setwarnings(False)

#Sets the output for the LED
RED = 21

#These tell the program where to output
GPIO.setmode(GPIO.BCM)  #BCM and PIN are your choices, all it does is tell the program what the numbers mean
        #BCM means you use a breadboard, PIN uses the actual PIN numbers of the circuit board
GPIO.setup(RED, GPIO.OUT)

#This code makes sure that the light is off at start
GPIO.output(RED,0)

#This code turns on the RED LED
GPIO.output(RED,1)
