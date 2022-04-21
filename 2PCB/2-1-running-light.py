import RPi.GPIO as GPIO
import time


def turn_on(leds):
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)
        


def turn_off(leds):
    GPIO.output(leds, 0)


leds = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

for times in range(3):
    turn_on(leds)
    turn_off(leds)

GPIO.cleanup()
