# #sudo apt install python3-rpi.gpio
# import RPi.GPIO as GPIO
# from time import sleep
# import sys



# def set_servo_angle(angle):
#     # Convert the angle to the appropriate duty cycle
#     duty = 2 + (angle / 18)  # For 0 to 180 degrees, adjust as needed
#     print(f"duty {duty}")
#     p.ChangeDutyCycle(duty)

# def move_servo_smoothly(start_angle, end_angle, speed):
#     step = 1 if start_angle < end_angle else -1  # Determine direction
#     for angle in range(start_angle, end_angle, step):
#         set_servo_angle(angle)
#         sleep(speed)  # Control the speed with the sleep time


# start_angle = int(sys.argv[1])
# end_angle = int(sys.argv[2])

# PIN_NUM= int(sys.argv[3]) #11 is x 13 is y
# # Set up GPIO and PWM
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(PIN_NUM, GPIO.OUT)
# p = GPIO.PWM(PIN_NUM, 50)  # 50Hz frequency for standard servo
# p.start(0)


# # Move the servo from 0 to 90 degrees, then back to 0
# move_servo_smoothly(start_angle, end_angle, 0.002)   # Move to 90 degrees with speed of 0.02s per degree


# # Clean up
# p.stop()
# GPIO.cleanup()                # At the end of the program, stop the PWM

# exit(0)





import RPi.GPIO as GPIO
from time import sleep
import sys
def set_servo_angle(angle):
    try:
        # Convert the angle to the appropriate duty cycle
        duty = 2 + (angle / 18)  # For 0 to 180 degrees, adjust as needed
        print(f"duty {duty}")
        p.ChangeDutyCycle(duty)
    except Exception as e:
        print(f"Error in set_servo_angle: {e}")
        cleanup_and_exit()


def move_servo_smoothly(start_angle, end_angle, speed):
    try:
        step = 1 if start_angle < end_angle else -1  # Determine direction
        for angle in range(start_angle, end_angle, step):
            set_servo_angle(angle)
            sleep(speed)  # Control the speed with the sleep time
    except Exception as e:
        print(f"Error in move_servo_smoothly: {e}")
        cleanup_and_exit()


def cleanup_and_exit():
    try:
        p.stop()
        GPIO.cleanup()  # Ensure GPIO cleanup
    except Exception as e:
        print(f"Error during cleanup: {e}")
    finally:
        exit(0)


try:
    # Read arguments
    start_angle = int(sys.argv[1])
    end_angle = int(sys.argv[2])
    PIN_NUM = int(sys.argv[3])  # 11 is x, 13 is y
    # Set up GPIO and PWM
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_NUM, GPIO.OUT)
    p = GPIO.PWM(PIN_NUM, 50)  # 50Hz frequency for standard servo
    p.start(0)

    # Move the servo
    move_servo_smoothly(start_angle, end_angle, 0.002)  # Move to 90 degrees with speed of 0.02s per degree

except ValueError as e:
    print(f"Invalid input: {e}")
    cleanup_and_exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    cleanup_and_exit()
finally:
    # Clean up at the end
    cleanup_and_exit()




























































































































































































































































































































































































































































































































































