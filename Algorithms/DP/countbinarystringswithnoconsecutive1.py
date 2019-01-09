def countbinary(n):

    a=[]
    b=[]
    a=[0 for x in range(n)]
    b=[0 for x in range(n)]
    a[0]=1
    b[0]=1

    for i in range(1,n):
        a[i]=a[i-1]+b[i-1]
        b[i]=a[i-1]
    
    print(a)
    print(b)
    print(a[i]+b[i])

if __name__ == "__main__":
    countbinary(4)