def mincut(s):
    n = len(s)
    palindrome = []
    palindrome = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        palindrome[i][i] = True

    for i in range(n-1):
        if s[i] == s[i+1]:
            palindrome[i][i+1] = True

    for currLen in range(3, n):
        for k in range(n-currLen+1):
            j = k+currLen-1
            if s[k] == s[j] and palindrome[k+1][j-1]:
                palindrome[k][j] = True

    print(palindrome)

    cuts = [0 for i in range(n)]
    for i in range(n):
        temp = 99999
        if palindrome[0][i]:
            cuts[i] = 0
        else:
            for j in range(i):
                if palindrome[j+1][i] and temp > cuts[j]+1:
                    temp = cuts[j]+1
            cuts[i] = temp
    print(cuts[n-1])

if __name__ == "__main__":
    mincut("bananna")
