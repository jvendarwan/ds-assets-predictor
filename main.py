from src.data_loader import fetch_market_data
from src.eda import run_eda

# Orchestrate the data loading, processing, training and evaluation pipeline
def main():
    # 1. Data collection
    data = fetch_market_data(verbose=True)
    if data is not None:
        data.to_csv('market_data.csv', index=False)

    # 2. EDA
    run_eda(data, save_figures=True, output_dir='figures') 

    # 3. Data processing

if __name__ == "__main__":
    main()
