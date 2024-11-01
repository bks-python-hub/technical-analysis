from nsepython import nse_eq

stock_data = nse_eq('ALL')
stock_names = [stock['symbol'] for stock in stock_data]

print(stock_names)