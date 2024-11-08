import RPi.GPIO as GPIO
from time import sleep
import sys

# Set up GPIO and PWM
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 50)  # 50Hz frequency for standard servo
p.start(0)

def set_servo_angle(angle):
    # Convert the angle to the appropriate duty cycle
    duty = 2 + (angle / 18)  # For 0 to 180 degrees, adjust as needed
    p.ChangeDutyCycle(duty)

def move_servo_smoothly(start_angle, end_angle, speed):
    step = 1 if start_angle < end_angle else -1  # Determine direction
    for angle in range(start_angle, end_angle, step):
        set_servo_angle(angle)
        sleep(speed)  # Control the speed with the sleep time


start_angle = int(sys.argv[1])
end_angle = int(sys.argv[2])

# Move the servo from 0 to 90 degrees, then back to 0
move_servo_smoothly(start_angle, end_angle, 0.005)   # Move to 90 degrees with speed of 0.02s per degree


# Clean up
p.stop()
GPIO.cleanup()                # At the end of the program, stop the PWM

exit(0)
