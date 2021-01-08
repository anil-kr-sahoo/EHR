import matplotlib.pyplot as plt
import pandas as pd

from bar_graph_plot import plot_bar_graph
from filter_inappropriate import filter_inappropriate_date
from pi_graph_plot import plot_pi_graph
from scattered_graph_plot import plot_scattered_graph
from user_input import input_given

plt.style.use("bmh")
# Preferred a gov portal for input data " https://www.stats.govt.nz/large-datasets/csv-files-for-download/  "
data_frame = pd.read_csv("serious-injury-outcome-indicators-2000-19.csv")


valid_data_series = list()
invalid_data_series = list()

all_series = data_frame['Series_reference']
remove_duplicates_series = list(set(all_series))

print("\nCorrupted Data List \n")

for data in remove_duplicates_series:
    appropriate_data = filter_inappropriate_date(data_frame, data)
    if appropriate_data:
        valid_data_series.append(data)
    else:
        invalid_data_series.append(data)

print("\nTotal Data Series We have "+str(len(remove_duplicates_series)))
print("\nTotal Invalid Data Series We have "+str(len(invalid_data_series)))
print("\nTotal Valid Data Series We have "+str(len(valid_data_series)))

# print(valid_data_series)

input_series = input_given(valid_data_series)
if not input_series:
    print("\n")
elif input_series not in valid_data_series:
    print("\n Invalid Preferred Series Given")
else:
    bar_graph = plt.figure(1)
    plot_bar_graph(plt, data_frame, input_series)
    scattered_graph = plt.figure(2)
    plot_scattered_graph(plt, data_frame, input_series)
    pi_graph = plt.figure(3)
    plot_pi_graph(plt, data_frame, input_series)
    plt.show()