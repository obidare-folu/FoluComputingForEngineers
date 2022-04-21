import RPi.GPIO as GPIO, time


def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]


def dec2dac(dec):
    GPIO.output(dac, dec2bin(dec))


def cleanup(lst):
    GPIO.output(lst, 0)
    GPIO.cleanup()


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    while True:
        for i in range(256):
            dec2dac(i)
            time.sleep(0.001)
        for i in range(255, -1, -1):
            dec2dac(i)
            time.sleep(0.001)

finally:
    cleanup(dac)
