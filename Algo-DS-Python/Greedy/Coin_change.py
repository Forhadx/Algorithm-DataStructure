# coin change problem
'''
give coins : [1, 2, 5, 20, 50, 100]

make money 201 with minimum  100, 100, 5 coins
'''

def coinChange(totalNumber , coin):
    num = totalNumber
    coin.sort()
    index = len(coin)-1

    while True:
        coinValue = coin[index]

        if num >= coinValue:
            print(coinValue)
            num -= coinValue
        
        if num < coinValue:
            index -= 1
        
        if num == 0:
            break


coins = [1, 2, 5, 20, 50, 100]

coinChange(201, coins) # 100 100 1