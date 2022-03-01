#input array containing the prices of a stock throught out the days
def buy_sell_stock(stocks: list[int]):
    buy = min(stocks)
    while stocks.index(buy) == len(stocks) - 1:
        stocks.remove(buy)
        buy = min(stocks)
    
    sell = max(stocks)
    while stocks.index(sell) < stocks.index(buy):
        stocks.remove(sell)
        sell = max(stocks)
    
    return f"Buy at {buy}\nSell at {sell}"

print(buy_sell_stock([7,2,5,3,1,0]))