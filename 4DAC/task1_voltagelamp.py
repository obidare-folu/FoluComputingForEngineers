import RPi.GPIO as GPIO


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
        dec = int(input("Input an integer in [0, 255]"))
        if dec > 255 or dec < 0:
            raise Exception("Number must be between 0 and 255 inclusive")
        
        dec2dac(dec)
        print(round(dec/256 * 3.3, 2))

finally:
    cleanup(dac)
