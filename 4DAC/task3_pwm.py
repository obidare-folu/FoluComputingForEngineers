import RPi.GPIO as GPIO


aux_pin = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(aux_pin, GPIO.OUT)
pwm = GPIO.PWM(aux_pin, 1000)


def cleanup(lst):
    GPIO.output(lst, 0)
    GPIO.cleanup()


try:
    while True:
        dec = int(input("Input duty cycle as percentage "))
        if dec > 100 or dec < 0:
            raise Exception("Number must be between 0 and 100 inclusive")
        pwm.start(dec)
        print(dec/100 * 3.3)


finally:
    cleanup(aux_pin)
