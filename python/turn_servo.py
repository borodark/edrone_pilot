from RPIO import PWM
import time

p = PWM.Servo()
p.set_servo(27, 1500)
pulse = 152
try:
    while 1:
	s = raw_input()
	delta = int(s)
	if delta == 0:
		pulse+=1
	elif delta == 9:
		pulse-=1
        p.set_servo(27,pulse*10)
        print('pulse = ', pulse*10)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop_servo(27)
