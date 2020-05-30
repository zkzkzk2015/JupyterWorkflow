import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD' 

def get_fremont_data(filename='fremont.csv', url=FREMONT_URL, force_download=False):

    """
    Download and cache the fremont.csv data

    Parameters:
    filename: string (optional)
        location to save the data
    url: string (optional)
        web location of the data
    force_download: bool (optional)
        if True, force redownload of data

    Returns:
    data: pandas DataFrame
        The fremont bridge data

    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('fremont.csv', parse_dates=True, index_col='Date')
    data.index = pd.to_datetime(data.index)
    data.columns = ['Total','West', 'East']
    data.resample('W').sum().plot();
    return data
