def plot_pi_graph(plt=None, data_frame=None, input_series=None):

    if plt is not None and data_frame is not None and input_series is not None:
        filter_referance = data_frame.loc[data_frame['Series_reference'] == input_series]
        x = filter_referance['Period']
        y = filter_referance['Data_value']
        explode_list = list()
        for d in range(len(x)):
            if d % 2 == 0:
                explode_list.append(.05)
            else:
                explode_list.append(.2)
        plt.pie(y, explode=explode_list, labels=x, autopct='%1.2f', startangle=90)
    else:
        pass