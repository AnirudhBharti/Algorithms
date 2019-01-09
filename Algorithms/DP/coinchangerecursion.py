def coinchangerecursion(amount, coins, coin):

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    nWays = 0
    for i in range(coin, len(coins)):
        nWays += coinchangerecursion(amount-coins[i], coins, i)

    return nWays

if __name__ == "__main__":
    coins = [1, 2]
    amount = 4
    print(coinchangerecursion(amount, coins, 0))
