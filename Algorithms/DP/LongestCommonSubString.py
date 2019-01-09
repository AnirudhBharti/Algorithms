def LongestCommonSubString(X, Y):
    m = len(X)
    n = len(Y)

    L = []
    L = [[0 for x in range(n+1)] for y in range(m+1)]

    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = 1+L[i-1][j-1]
                result =  max(result,  L[i][j])
            else:
                L[i][j] = 0

    print(result)


if __name__ == "__main__":
    X = "OldSite:GeeksforGeeks.org"
    Y = "NewSite:GeeksQuiz.com"
    LongestCommonSubString(X, Y)
