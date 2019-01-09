def mincoinsum(coins,sum):
    k=sum+1
    i=len(coins)
    minArray = [[0 for x in range(k)] for u in range(i)]
    for u in range(i):
        minArray[u][0]=1
    

   
    for coin in range(1,len(coins)):
        for j in range(1,k):
            if j >= coins[coin-1]:
                minArray[coin][j] = 1+min(minArray[coin-1][j], minArray[coin][j-coins[coin-1]])
            else:
               minArray[coin][j]  = minArray[coin-1][j]
    
    print(minArray)
    return minArray[coin][j]

if __name__ == "__main__":
    coins=[9, 6, 5, 1]
    sum = 11
    print(mincoinsum(coins,sum))