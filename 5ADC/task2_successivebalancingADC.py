import RPi.GPIO as GPIO, time


dac = [26, 19, 13, 6, 5, 11, 9, 10]
input_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]


def dec2dac(dec):
    GPIO.output(dac, dec2bin(dec))


def cleanup(lst):
    GPIO.output(lst, 0)
    GPIO.cleanup()


def adc():
    bits = [0] * 8
    for i in range(8):
        bits_copy = bits.copy()
        bits_copy[i] = 1
        GPIO.output(dac, bits_copy)
        time.sleep(0.001)
        bits[i] = GPIO.input(input_pin)
            

    GPIO.output(dac, bits)
    time.sleep(0.01)
    digital = 0
    for i, value in enumerate(bits):
        digital = digital + (2**(7 - i) * value)
    analogue = round(digital/256 * 3.3, 2)
    return [digital, analogue]

try:
    while True:
        print(adc())

finally:
    cleanup(17)
    cleanup(dac)
    