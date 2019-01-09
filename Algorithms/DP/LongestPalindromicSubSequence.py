def LPS(str):
    length = len(str)
    dp = []
    dp = [[0 for n in range(length)] for m in range(length)]

    for k in range(length):
        dp[k][k] = 1

    for i in range(length-2, -1, -1):
        for j in range(i+1, length):
            if str[i] == str[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])

    print("LPS length is ", dp[0][length-1])


    for n in range(7,17): 
        print(n)
    
    screen = [0]*7
    print(screen)
if __name__ == "__main__":
    LPS("BAABS")
    LPS("GEEKSFORGEEKS")
    LPS("banana")
