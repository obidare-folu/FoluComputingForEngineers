import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)



leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [2, 3, 14, 15, 18, 27, 23, 22]
aux.reverse()

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
    while True:
        for index, i in enumerate(aux):
            GPIO.output(leds[index], GPIO.input(i))

finally:
    GPIO.output(leds, [0] * len(leds))
    GPIO.cleanup()
