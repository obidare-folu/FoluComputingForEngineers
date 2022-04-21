import RPi.GPIO as GPIO
import time


def binary(num):
    a = '{0:08b}'.format(num)
    lst = [int(i) for i in a]
    return lst



dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

number = [0, 5, 32, 64, 127, 255]

for i in number:
    GPIO.output(dac, binary(i))
    time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
