import RPi.GPIO as GPIO, time
import matplotlib.pyplot as plt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
input_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(input_pin, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def dec2bin(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(8)]


def dec2dac(dec):
    GPIO.output(dac, dec2bin(dec))


def cleanup(lst):
    GPIO.output(lst, 0)
    GPIO.cleanup()


def output_to_leds(digital):
    num_turned_on_light = (8 * digital) // 250
    output = [0] * 8
    for i, value in enumerate(output[8 - num_turned_on_light:]):
        output[i] = 1
    output.reverse()
    GPIO.output(leds, output)

def adc():
    bits = [0] * 8
    for i in range(8):
        bits_copy = bits.copy()
        bits_copy[i] = 1
        GPIO.output(dac, bits_copy)
        time.sleep(0.001)
        bits[i] = GPIO.input(input_pin)
            

    GPIO.output(dac, bits)
    digital = 0
    for i, value in enumerate(bits):
        digital = digital + (2**(7 - i) * value)
    analogue = round(digital/256 * 3.3, 2)
    return [digital, analogue]

try:
    GPIO.output(17, 1)

    start_charging_time = time.time()
    fully_charged_time = None
    discharge_time = None

    digital_values = list()

    while True:
        adc_var = (adc()) # adc algorithm with successive approximation
        print(adc_var)
        digital_values.append(adc_var[0])
        output_to_leds(adc_var[0])

        if adc_var[0] >= 250: # Capacitor is almost fully charged so store time and output 0 to pin
            fully_charged_time = time.time()
            GPIO.output(17, 0)
            
        if digital_values[-1] == 2 and fully_charged_time is not None: # capacitor is discharged so save time and stop reading values
            discharge_time = time.time()
            break

    print("\n\nTotal time to charge:", round(fully_charged_time - start_charging_time))
    print("Total time to discharge:", round(discharge_time - fully_charged_time))
    print("Theoretical time to charge and discharge = 100 seconds. Real time =", round(discharge_time - start_charging_time))

    # store data and settings into files
    measured_adc_data = [str(digital) for digital in digital_values]
    with open("data.txt", 'w') as outfile:
        outfile.write("\n".join(measured_adc_data))

    with open("settings.txt", 'w') as settingsfile:
        settingsfile.write("Experiment duration:\t{}\n".format(str(round(discharge_time - start_charging_time))))
        settingsfile.write("Voltage step:\t{}\n".format(str(3.3 / 256)))

    plt.plot(digital_values)
    plt.show()

finally:
    cleanup(17)
    cleanup(dac)

