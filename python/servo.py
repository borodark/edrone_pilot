"""
Demonstration of how to control servo pulses with RPIO.PWM
RPIO Documentation: http://pythonhosted.org/RPIO
"""
from RPIO import PWM
import time

servo = PWM.Servo()

# Add servo pulse for GPIO 17 with 1200 (1.2ms)
servo.set_servo(27, 1300)
time.sleep(10)
# Add servo pulse for GPIO 17 with 2000 (2.0ms)
servo.set_servo(27, 2000)

# Clear servo on GPIO17
servo.stop_servo(27)


