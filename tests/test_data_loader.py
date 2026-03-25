import pandas as pd
from unittest.mock import patch
from src.data_loader import fetch_asset_data, align_dataframes, process_market_data, fetch_market_data

# Sample data for mocking
def make_sample_df(index, open_val, high_val, low_val, close_val, volume_val):
    return pd.DataFrame({
        'Open': [open_val] * len(index),
        'High': [high_val] * len(index),
        'Low': [low_val] * len(index),
        'Close': [close_val] * len(index),
        'Volume': [volume_val] * len(index),
    }, index=index)

def test_align_dataframes():
    idx = pd.date_range('2020-01-01', periods=3)
    df1 = pd.DataFrame({'A': [1, 2, 3]}, index=idx)
    df2 = pd.DataFrame({'A': [4, 5]}, index=idx[:2])
    aligned, = align_dataframes(df1, df2)
    assert all(aligned.index == df1.index)
    # After forward fill, the last value should be the same as the previous one
    assert aligned.iloc[-1, 0] == aligned.iloc[-2, 0]
    # There should be no NaNs after forward fill
    assert aligned.isnull().sum().sum() == 0

@patch('src.data_loader.yf.download')
def test_fetch_asset_data(mock_download):
    idx = pd.date_range('2020-01-01', periods=2)
    df = make_sample_df(idx, 1, 2, 0, 1.5, 100)
    mock_download.return_value = df
    
    result = fetch_asset_data('BTC-USD', '2020-01-01', '2020-01-03', verbose=False)
    
    pd.testing.assert_frame_equal(result, df)

@patch('src.data_loader.fetch_asset_data')
def test_fetch_market_data_success(mock_fetch):
    idx = pd.date_range('2020-01-01', periods=2)
    btc = make_sample_df(idx, 1, 2, 0, 1.5, 100)
    nasdaq = make_sample_df(idx, 10, 20, 5, 15, 200)
    gold = make_sample_df(idx, 100, 200, 50, 150, 300)
    mock_fetch.side_effect = [btc, nasdaq, gold]

    data = fetch_market_data('2020-01-01', '2020-01-03', verbose=False)

    assert data is not None
    assert 'BTC Close' in data.columns
    assert 'NASDAQ Close' in data.columns
    assert 'Gold Close' in data.columns
    assert 'Trend' in data.columns
    assert len(data) == 2

@patch('src.data_loader.fetch_asset_data')
def test_fetch_market_data_empty(mock_fetch):
    idx = pd.date_range('2020-01-01', periods=2)
    empty = pd.DataFrame()
    btc = make_sample_df(idx, 1, 2, 0, 1.5, 100)
    mock_fetch.side_effect = [btc, empty, empty]

    data = fetch_market_data('2020-01-01', '2020-01-03', verbose=False)

    assert data is None

def test_process_market_data():
    idx = pd.date_range('2020-01-01', periods=2)
    btc = make_sample_df(idx, 1, 2, 0, 1.5, 100)
    nasdaq = make_sample_df(idx, 10, 20, 5, 15, 200)
    gold = make_sample_df(idx, 100, 200, 50, 150, 300)
    # Add required columns for gold
    gold['Gold Low'] = gold['Low']
    gold['Gold Close'] = gold['Close']

    data = process_market_data(btc, nasdaq, gold)

    assert 'BTC Open' in data.columns
    assert 'NASDAQ Open' in data.columns
    assert 'Gold Open' in data.columns
    assert 'Trend' in data.columns
    assert all(data['Trend'].isin([-1, 1]))
