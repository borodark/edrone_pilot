import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

p23 = GPIO.PWM(23, 1500)  # channel=25 frequency=50Hz
p24 = GPIO.PWM(24, 1500)  # channel=25 frequency=50Hz
p23.start(0)
p24.start(0)

try:
    while 1:
	time.sleep(1)
        for dc in range(0, 100, 1):
		print("dc= ",dc)
            	p23.ChangeDutyCycle(dc)
            	p24.ChangeDutyCycle(dc)
		time.sleep(1)
       	print("At Maximum!! decreasing duty cycle")
	time.sleep(1) 
	for dc in range(100, 0, -1):
		print("dc= ",dc)	
      		p23.ChangeDutyCycle(dc)
            	p24.ChangeDutyCycle(dc)
		time.sleep(1)
	print("At Minimum!! decreasing duty cycle")	
except KeyboardInterrupt:
    pass
p23.stop()
p24.stop()
GPIO.cleanup()

