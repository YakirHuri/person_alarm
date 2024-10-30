from gpiozero import Servo
from time import sleep


from gpiozero import Servo, Device
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(17, pin_factory=factory)  # Replace 17 with your GPIO pin number



servo.mid()

