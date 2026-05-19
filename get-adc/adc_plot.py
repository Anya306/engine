from matplotlib import pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title('Зависимость напряжения от времени', fontsize=14)
    plt.xlabel('Bрeмя, с', fontsize=12)
    plt.ylabel('Напряжение, В', fontsize=12)
    plt.grid()
    plt.xlim(min(time) - 0.05, max(time) + 0.05)
    plt.ylim(0, max_voltage * 1.05)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_period = []
    for i in range(1, len(time)):
        sampling_period.append(time[i] - time[i - 1])
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_period)
    plt.title('Распределение периодов дискретизации')
    plt.xlabel('Bрeмя, с')
    plt.ylabel('Количество измерений')
    plt.grid()
    plt.xlim(0, 0.06)
    plt.show()