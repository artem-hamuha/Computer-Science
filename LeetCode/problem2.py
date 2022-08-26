def bestBuySell(prices):
    max = 0
    last = prices[0]

    for i in range(1, len(prices)):
        if prices[i] > last:
            max += prices[i] - last
            last = prices[i]
        
        else:
            last = prices[i]

    print(max)

bestBuySell([7,1,5,3,6,4])