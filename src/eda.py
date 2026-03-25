import os
import matplotlib.pyplot as plt
import seaborn as sns

def print_basic_info(data):
    print("1. Basic Data Information")
    print("\nDataset Shape:", data.shape)
    print("\nData Types:")
    print(data.dtypes)
    print("\nMissing Values:")
    print(data.isnull().sum())

def plot_time_series(data, save_figures=False, output_dir='figures'):
    plt.figure(figsize=(15, 8))
    plt.plot(data['Date'], data['BTC Close'], label='Bitcoin', alpha=0.7)
    plt.plot(data['Date'], data['NASDAQ Close'], label='NASDAQ', alpha=0.7)
    plt.plot(data['Date'], data['Gold Close'], label='Gold', alpha=0.7)
    plt.title('Price Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'price_trends.png'))
        plt.close()
    else:
        plt.show()

def plot_correlation_matrix(data, save_figures=False, output_dir='figures'):
    correlation_matrix = data[['BTC Close', 'NASDAQ Close', 'Gold Close']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Closing Prices')
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'correlation_matrix.png'))
        plt.close()
    else:
        plt.show()

def plot_returns_correlation(data, save_figures=False, output_dir='figures'):
    data['BTC Returns'] = data['BTC Close'].pct_change()
    data['NASDAQ Returns'] = data['NASDAQ Close'].pct_change()
    data['Gold Returns'] = data['Gold Close'].pct_change()
    returns_corr = data[['BTC Returns', 'NASDAQ Returns', 'Gold Returns']].corr()
    print(returns_corr)
    plt.figure(figsize=(10, 8))
    sns.heatmap(returns_corr, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Matrix of Daily Returns')
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'returns_correlation_matrix.png'))
        plt.close()
    else:
        plt.show()

def plot_volume_trends(data, save_figures=False, output_dir='figures'):
    plt.figure(figsize=(15, 8))
    plt.plot(data['Date'], data['BTC Volume'], label='Bitcoin Volume', alpha=0.7)
    plt.plot(data['Date'], data['NASDAQ Volume'], label='NASDAQ Volume', alpha=0.7)
    plt.plot(data['Date'], data['Gold Volume'], label='Gold Volume', alpha=0.7)
    plt.title('Trading Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.legend()
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'volume_trends.png'))
        plt.close()
    else:
        plt.show()

def plot_price_ranges(data, save_figures=False, output_dir='figures'):
    data['BTC Range'] = data['BTC High'] - data['BTC Low']
    data['NASDAQ Range'] = data['NASDAQ High'] - data['NASDAQ Low']
    data['Gold Range'] = data['Gold High'] - data['Gold Low']
    plt.figure(figsize=(15, 8))
    plt.plot(data['Date'], data['BTC Range'], label='Bitcoin Range', alpha=0.7)
    plt.plot(data['Date'], data['NASDAQ Range'], label='NASDAQ Range', alpha=0.7)
    plt.plot(data['Date'], data['Gold Range'], label='Gold Range', alpha=0.7)
    plt.title('Daily Price Ranges Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price Range')
    plt.legend()
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'price_ranges.png'))
        plt.close()
    else:
        plt.show()

def plot_returns_distributions(data, save_figures=False, output_dir='figures'):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    sns.histplot(data['BTC Returns'].dropna(), ax=axes[0], bins=50)
    axes[0].set_title('Bitcoin Returns Distribution')
    sns.histplot(data['NASDAQ Returns'].dropna(), ax=axes[1], bins=50)
    axes[1].set_title('NASDAQ Returns Distribution')
    sns.histplot(data['Gold Returns'].dropna(), ax=axes[2], bins=50)
    axes[2].set_title('Gold Returns Distribution')
    plt.tight_layout()
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'returns_distributions.png'))
        plt.close()
    else:
        plt.show()

def plot_trend_distribution(data, save_figures=False, output_dir='figures'):
    trend_counts = data['Trend'].value_counts()
    plt.figure(figsize=(8, 6))
    trend_counts.plot(kind='bar')
    plt.title('Distribution of Price Trends')
    plt.xlabel('Trend (-1: Down, 1: Up)')
    plt.ylabel('Count')
    if save_figures:
        os.makedirs(output_dir, exist_ok=True)
        plt.savefig(os.path.join(output_dir, 'trend_distribution.png'))
        plt.close()
    else:
        plt.show()

def print_summary_statistics(data):
    print("\n9. Summary Statistics")
    print("\nBitcoin Price Statistics:")
    print(data['BTC Close'].describe())
    print("\nNASDAQ Price Statistics:")
    print(data['NASDAQ Close'].describe())
    print("\nGold Price Statistics:")
    print(data['Gold Close'].describe())

def run_eda(data, save_figures=False, output_dir='figures'):
    plt.style.use('seaborn')
    sns.set_palette('husl')
    print_basic_info(data)
    plot_time_series(data, save_figures, output_dir)
    plot_correlation_matrix(data, save_figures, output_dir)
    plot_returns_correlation(data, save_figures, output_dir)
    plot_volume_trends(data, save_figures, output_dir)
    plot_price_ranges(data, save_figures, output_dir)
    plot_returns_distributions(data, save_figures, output_dir)
    plot_trend_distribution(data, save_figures, output_dir)
    print_summary_statistics(data) 