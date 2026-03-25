import pandas as pd
from unittest.mock import patch
from src.eda import (
    print_basic_info, plot_time_series, plot_correlation_matrix, plot_returns_correlation,
    plot_volume_trends, plot_price_ranges, plot_returns_distributions, plot_trend_distribution,
    print_summary_statistics, run_eda
)

def make_sample_eda_df():
    idx = pd.date_range('2020-01-01', periods=3)
    df = pd.DataFrame({
        'Date': idx,
        'BTC Open': [1, 2, 3],
        'BTC High': [2, 3, 4],
        'BTC Low': [0.5, 1.5, 2.5],
        'BTC Close': [1.5, 2.5, 3.5],
        'BTC Volume': [100, 110, 120],
        'NASDAQ Open': [10, 11, 12],
        'NASDAQ High': [11, 12, 13],
        'NASDAQ Low': [9, 10, 11],
        'NASDAQ Close': [10.5, 11.5, 12.5],
        'NASDAQ Volume': [200, 210, 220],
        'Gold Open': [100, 101, 102],
        'Gold High': [101, 102, 103],
        'Gold Low': [99, 100, 101],
        'Gold Close': [100.5, 101.5, 102.5],
        'Gold Volume': [300, 310, 320],
        'Trend': [1, -1, 1],
    })
    df['BTC Returns'] = df['BTC Close'].pct_change()
    df['NASDAQ Returns'] = df['NASDAQ Close'].pct_change()
    df['Gold Returns'] = df['Gold Close'].pct_change()
    return df

def test_print_basic_info(capsys):
    df = make_sample_eda_df()
    print_basic_info(df)
    captured = capsys.readouterr()
    assert "Basic Data Information" in captured.out
    assert "Dataset Shape" in captured.out

def test_print_summary_statistics(capsys):
    df = make_sample_eda_df()
    print_summary_statistics(df)
    captured = capsys.readouterr()
    assert "Summary Statistics" in captured.out
    assert "Bitcoin Price Statistics" in captured.out
    assert "NASDAQ Price Statistics" in captured.out
    assert "Gold Price Statistics" in captured.out

@patch("matplotlib.pyplot.show")
def test_plot_time_series_show(mock_show):
    df = make_sample_eda_df()
    plot_time_series(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_time_series_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_time_series(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_correlation_matrix_show(mock_show):
    df = make_sample_eda_df()
    plot_correlation_matrix(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_correlation_matrix_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_correlation_matrix(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_returns_correlation_show(mock_show):
    df = make_sample_eda_df()
    plot_returns_correlation(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_returns_correlation_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_returns_correlation(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_volume_trends_show(mock_show):
    df = make_sample_eda_df()
    plot_volume_trends(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_volume_trends_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_volume_trends(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_price_ranges_show(mock_show):
    df = make_sample_eda_df()
    plot_price_ranges(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_price_ranges_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_price_ranges(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_returns_distributions_show(mock_show):
    df = make_sample_eda_df()
    plot_returns_distributions(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_returns_distributions_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_returns_distributions(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_plot_trend_distribution_show(mock_show):
    df = make_sample_eda_df()
    plot_trend_distribution(df, save_figures=False)
    mock_show.assert_called_once()

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_plot_trend_distribution_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    plot_trend_distribution(df, save_figures=True, output_dir="test_figures")
    mock_savefig.assert_called_once()
    mock_close.assert_called_once()

@patch("matplotlib.pyplot.show")
def test_run_eda_show(mock_show):
    df = make_sample_eda_df()
    run_eda(df, save_figures=False)
    assert mock_show.call_count > 0

@patch("matplotlib.pyplot.savefig")
@patch("matplotlib.pyplot.close")
def test_run_eda_save(mock_close, mock_savefig):
    df = make_sample_eda_df()
    run_eda(df, save_figures=True, output_dir="test_figures")
    assert mock_savefig.call_count > 0
    assert mock_close.call_count > 0 