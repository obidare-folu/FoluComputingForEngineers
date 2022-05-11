import matplotlib.pyplot as plt
import numpy as np


try:
    # import date and settings
    data_array = np.loadtxt('data.txt', dtype=int)
    with open('settings.txt', 'r') as settingsfile:
        settings = [(i.split('\t')[0], float(i.split('\t')[1])) for i in settingsfile.read().split('\n')]

    # Converting ADC outputs to Volts and seconds.
    voltages = settings[1][1]*data_array
    time = [settings[0][1]/len(voltages) * i for i in range(len(voltages))]

    fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

    # plot title centered and wraped
    title = 'The process of charging and discharging a capacitor in an RC circuit'
    ax.set_title(title, loc='center', wrap=True)

    graph = ax.plot(time, voltages, 'g.', linestyle='-', label="Voltage")

    # grid
    xticks = np.arange(0, 100, 10)
    ax.set_xticks(xticks)
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

    # plot legend
    ax.legend()

    # axes min and max setup
    plt.xlim(min(time),max(time) + 1)
    plt.ylim(min(voltages),max(voltages) + 0.2)

    # text added to plot
    plt.text(0.85, 0.55, 'Total time to charge = 46sec',
            verticalalignment='bottom', horizontalalignment='right',
            transform=ax.transAxes,
            color='blue', fontsize=10)
    plt.text(0.865, 0.5, 'Total time to discharge = 54sec',
            verticalalignment='bottom', horizontalalignment='right',
            transform=ax.transAxes,
            color='blue', fontsize=10)

    # axes labelled
    plt.ylabel('Voltage (V)')
    plt.xlabel('Time (sec)')

    # save file
    fig.savefig("graph.svg")

    plt.show()

finally:
    datafile.close()
    settingsfile.close()
