import RPi.GPIO as GPIO
import time


pin = 26
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)


try:
    i = 1
    while True:
        GPIO.output(pin, i)
        i = (i-1)*-1
        time.sleep(0.5)

# except KeyboardInterrupt:
#     print("Time to turn off diode223")
#     GPIO.output(pin, 0)
finally:
    print("Time to turn off diode")
    GPIO.output(pin, 0)
    GPIO.cleanup()
