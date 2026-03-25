import yfinance as yf
import pandas as pd
from rich.console import Console

console = Console()

def fetch_asset_data(ticker, start_date, end_date, verbose=True):
    if verbose:
        console.print(f"[bold yellow]Fetching {ticker} data...[/bold yellow]")
    df = yf.download(ticker, start=start_date, end=end_date, progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df = df.xs(ticker, level='Ticker', axis=1)
    return df

def align_dataframes(reference_df, *dfs):
    aligned = [df.reindex(reference_df.index, method='ffill') for df in dfs]
    return aligned

def process_market_data(btc, nasdaq, gold):
    data = pd.DataFrame(index=btc.index)
    data['Date'] = data.index
    # Bitcoin
    data['BTC Open'] = btc['Open'].round(6)
    data['BTC High'] = btc['High'].round(6)
    data['BTC Low'] = btc['Low'].round(6)
    data['BTC Close'] = btc['Close'].round(6)
    data['BTC Volume'] = btc['Volume'].astype(int)
    # NASDAQ
    data['NASDAQ Open'] = nasdaq['Open'].round(6)
    data['NASDAQ High'] = nasdaq['High'].round(6)
    data['NASDAQ Low'] = nasdaq['Low'].round(6)
    data['NASDAQ Close'] = nasdaq['Close'].round(6)
    data['NASDAQ Volume'] = nasdaq['Volume'].astype(int)
    # Gold
    data['Gold Open'] = gold['Open'].round(1)
    data['Gold High'] = gold['High'].round(1)
    data['Gold Low'] = gold['Low'].round(1)
    data['Gold Close'] = gold['Close'].round(1)
    data['Gold Volume'] = gold['Volume'].astype(int)
    # Trend
    data['Trend'] = (data['BTC Close'] > data['BTC Open']).astype(int) * 2 - 1
    return data

def fetch_market_data(start_date='2014-09-17', end_date='2025-06-09', verbose=True):
    try:
        if verbose:
            console.print("[bold yellow]🔍 Fetching market data...[/bold yellow]")
            console.print(f"[bold]📅 Date range:[/bold] {start_date} to {end_date}")
        btc = fetch_asset_data('BTC-USD', start_date, end_date, verbose)
        nasdaq = fetch_asset_data('^IXIC', start_date, end_date, verbose)
        gold = fetch_asset_data('GC=F', start_date, end_date, verbose)
        if btc.empty or nasdaq.empty or gold.empty:
            if verbose:
                console.print("[bold red]⚠️ Warning: One or more dataframes are empty![/bold red]")
            return None
        nasdaq, gold = align_dataframes(btc, nasdaq, gold)
        data = process_market_data(btc, nasdaq, gold)
        if verbose:
            console.print("[bold green]✅ Data processing complete![/bold green]")
        return data
    except Exception as e:
        if verbose:
            console.print(f"[bold red]❌ An error occurred: {str(e)}[/bold red]")
        import traceback
        traceback.print_exc()
        return None