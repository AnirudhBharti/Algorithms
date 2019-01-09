def LongestCommonSubsequence(X, Y):
    m = len(X)
    n = len(Y)

    L = []
    L = [[0 for x in range(n+1)] for y in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1]==Y[j-1]:
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j],L[i][j-1])
    
    print(L[i][j])

if __name__ == "__main__":
    X="AGGTAB"
    Y="GXTXAYB"
    LongestCommonSubsequence(X,Y)