def plot_bar_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Series_reference'] == input_series]
        x = filter_referance['Period']
        y = filter_referance['Data_value']
        plt.xlabel("Year", fontsize=18)
        plt.ylabel("Injury", fontsize=18)
        plt.bar(x, y)
    else:
        pass