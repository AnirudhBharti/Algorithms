def ManachersLPS(s):

    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0]*n

    R = 0
    C = 0
    for i in range(1, n-1):
        mirror = 2*C - i

        if i < R:
            P[i] = min(R-i, P[mirror])

        # expand arround center
        while T[i+(1+P[i])] == T[i-(1+P[i])]:
            P[i] += 1

        if i+P[i] > R:
            C = i
            R = i+P[i]

    print(P)
    maxLen, centerIndex = max((n,i) for i, n in enumerate(P))
    print(maxLen, centerIndex)
  
  

if __name__ == "__main__":
    ManachersLPS("ABABABA")
