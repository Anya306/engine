import r2r_adc
import time
import adc_plot

voltage_values = []
time_values = []
duration = 3.0
dynamic_range = 3.2
try:
    adc = r2r_adc.R2R_ADC(dynamic_range, compare_time=0.001)
    begin = time.time()
    while time.time() - begin < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - begin)
    adc_plot.plot_voltage_vs_time(time_values, voltage_values, 3.2)
    adc_plot.plot_sampling_period_hist(time_values)

finally:
    adc.deinit()