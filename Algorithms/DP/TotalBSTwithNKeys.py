def BST(n):

    c = []
    c = [0 for x in range(n+1)]
    c[0] = c[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            c[i] += c[j]*c[i-j-1]

    print(c[i])


def BSTR(n):
    if n == 0 or n == 1:
        return 1
    else:
        nums=0
        for i in range(2,n+1):
            nums+= BSTR(i-1)*BSTR(n-i)
        return nums

    


if __name__ == "__main__":
    print(BSTR(6))
