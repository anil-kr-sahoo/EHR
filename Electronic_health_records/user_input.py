import PySimpleGUI as sg


def input_given(data_list=None):
    if data_list:
        form = sg.FlexForm('Select Your Series Reference')
        start_index = 0
        layout = list()

        while True:
            if start_index >= len(data_list):
                break
            else:
                end_index = start_index + 10
                if end_index >= len(data_list):
                    end_index = len(data_list)
                layout.append([sg.Text(data_list[start_index: end_index])])
                start_index += 10

        layout.append([sg.Text('')])
        layout.append([sg.Text('Type Your Reference Series', size=(15, 1)), sg.InputText('')])
        layout.append([sg.Submit(), sg.Cancel()])

        button, values = sg.Window.Layout(self=form, rows=layout).Read()
        if button == "Cancel":
            print('\nThankYou for Using our Software')
        else:
            sg.Window.Close(self=form)
            return values[0]
    else:
        pass
