def coinchange(coins, amount):
    print('coin change problem')
    combinations = [0 for x in range(amount+1)]
    combinations[0] = 1
    for coin in range(len(coins)):
        for i in range(len(combinations)):
            if i >= coins[coin]:
                combinations[i]+=combinations[i-coins[coin]]

    return combinations[i]
if __name__=="__main__":
    coins = [1,2]
    amount = 4
    print(coinchange(coins, amount))
