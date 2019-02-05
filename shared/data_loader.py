import pandas as pd

def dparserfunc(date):
    return pd.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')

def load_data(path):
    data = pd.read_csv(path, index_col='Time', parse_dates=True, sep=',', usecols=['Time', 'prod08.ld5'], squeeze=True, date_parser=dparserfunc)
    return data

def data_it(raw_data, block_size = 20):
    for i in range(len(raw_data) - block_size):
        eval_data = raw_data[i : i + block_size]
        yield eval_data