from jupyterworkflow.data import get_fremont_data
import pandas as pd

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['Total', 'West', 'East'])
    assert isinstance(data.index, pd.DatetimeIndex)
