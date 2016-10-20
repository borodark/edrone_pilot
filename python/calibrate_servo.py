from RPIO import PWM
import time

p = PWM.Servo()
p.set_servo(27, 1500)
try:
    while 1:
	s = raw_input()
	pulse = int(s)
        p.set_servo(27,pulse*10)
        print('pulse = ', pulse*10)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop_servo(27)
