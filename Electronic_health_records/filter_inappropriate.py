def filter_inappropriate_date(data_frame=None, series=None):

    if series and not data_frame.empty:
        filter_referance = data_frame.loc[data_frame['Series_reference'] == series]
        x = filter_referance['Period']
        for data in x:
            if "-" in data:
                print(data,"--------------",series)
                return False
        return True