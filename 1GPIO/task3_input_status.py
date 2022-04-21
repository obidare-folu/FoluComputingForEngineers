import RPi.GPIO as GPIO
import time


input_pin = 26
output_pin_for_led = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(output_pin_for_led, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN)

try:
    if GPIO.input(input_pin):
        GPIO.output(output_pin_for_led, 1)
    else:
        GPIO.output(output_pin_for_led, 0)

finally:
    time.sleep((10))
    GPIO.output(output_pin_for_led, 0)
    GPIO.cleanup()
