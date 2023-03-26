import yfinance as yf
import pandas as pd
import os.path

# Create a list of ticker symbols
tickers = ["MSFT", "AAPL", "TSLA"]

# Create a new DataFrame to store the data
df = pd.DataFrame()

# Loop through the ticker symbols
for ticker in tickers:

    # Get the historical data for the ticker symbol
    msft = yf.Ticker(ticker)
    msft_history = msft.history(period="1d")

    # Store the closing price for the ticker symbol in a DataFrame
    df = df.append({"Ticker": ticker, "Date": msft_history.index[0].tz_localize(None), "Close": msft_history["Close"][0]}, ignore_index=True)

# Check if the Excel file already exists
if os.path.isfile("MSFT_prices.xlsx"):
    # Read the existing Excel file
    existing_data = pd.read_excel("MSFT_prices.xlsx", sheet_name="MSFT", index_col=None)

    # Check if the 'Ticker' column exists in the existing data
    if 'Ticker' not in existing_data.columns:
        # Add the 'Ticker' column to the existing data
        existing_data['Ticker'] = [ticker] * len(existing_data)

    # Append the new data to the existing data
    updated_data = existing_data.append(df, ignore_index=True)

    # Save the updated data to the Excel file
    with pd.ExcelWriter("MSFT_prices.xlsx", engine="openpyxl") as writer:
        updated_data.to_excel(writer, sheet_name="MSFT", index=False)

else:
    # Sort the DataFrame by ticker
    df = df.sort_values(by="Ticker")

    # Save the DataFrame to a new Excel file
    df.to_excel("MSFT_prices.xlsx", sheet_name="MSFT", index=False)
