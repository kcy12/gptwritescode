import yfinance as yf
from colorama import Fore, Style, init

init(autoreset=True)

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
            
            current_price = info['regularMarketPrice']
            previous_close = info['regularMarketPreviousClose']
            
            
            if current_price > previous_close:
                price_color = Fore.GREEN
            elif current_price < previous_close:
                price_color = Fore.RED
            else:
                price_color = Fore.WHITE

            print("Current Price: {}{}".format(price_color, current_price))
            print("Previous Close: {}".format(previous_close))

            
        

        except Exception as e:
            print("Error: Unable to fetch quote for {}. Please try again with a valid symbol.\n".format(symbol.upper()))

if __name__ == "__main__":
    main()
