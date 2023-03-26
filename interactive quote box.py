import yfinance as yf

def get_quote(symbol):
    ticker = yf.Ticker(symbol)
    info = ticker.info
    return info

def main():
    print("Welcome to the Simple Quote Generator!")
    while True:
        symbol = input("Enter a stock symbol to get a quote (or type 'exit' to quit): ")
        if symbol.lower() == "exit":
            break
        
        try:
            info = get_quote(symbol)
            print("\nQuote for {}: \n".format(symbol.upper()))
            print("Name: {}".format(info['longName']))
            print("Symbol: {}".format(info['symbol']))
            print("Market: {}".format(info['market']))
            print("Exchange: {}".format(info['exchange']))
            print("Currency: {}".format(info['currency']))
            print("Current Price: {}".format(info['regularMarketPrice']))
            print("Previous Close: {}\n".format(info['regularMarketPreviousClose']))
        except Exception as e:
            print("Error: Unable to fetch quote for {}. Please try again with a valid symbol.\n".format(symbol.upper()))

if __name__ == "__main__":
    main()
