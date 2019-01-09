def subsetofmatrixofones(M):
    R =  len(M)
    C = len(M[0])
    S = [[0 for k in range(C)] for l in range(R)]
    maxVal=0
    p=0
    q=0
    for i in range(1,R):
        for j in range(1,C):
            if(M[i][j]==1):
                S[i][j]=min(S[i-1][j],S[i][j-1],S[i-1][j-1])+1
                if(S[i][j] > maxVal):
                    maxVal = S[i][j]
                    p=i
                    q=j
            else:
                S[i][j]=0

    print(maxVal)
    print('index i =>',p,'index j =>',q)

    beginIndex = p
    endIndex = q
    while(beginIndex > 0 and endIndex > 0):
        if(M[beginIndex-1][endIndex-1]==0):
            break
        beginIndex = beginIndex-1
        endIndex = endIndex-1   
       

      
    print(beginIndex,'====>',endIndex)
    z = [[0 for c in range(p+1)] for r in range(q+1)]

    for m in range(beginIndex, p+1):
        for n in range(endIndex, q+1):
            z[m][n] = M[m][n]
  
    print(z)
if __name__ == "__main__":
    print('hello python')
    # M=[
    #     [1,1,1,0,1],
    #     [1,1,1,0,0],
    #     [1,1,1,1,0],
    #     [0,0,0,1,0],
    #     [0,0,0,0,0],
    #     ]

    M=[
        [1,1,1,1,1],
        [1,1,1,1,0],
        [1,1,1,1,0],
        [1,1,1,1,0],
        [0,0,0,0,0],
        ]

    # M=[
    #     [0,0,0,0,1],
    #     [0,1,1,1,0],
    #     [0,1,1,1,0],
    #     [0,1,1,1,0],
    #     [0,0,0,0,0],
    #     ]
    
    # M=[
    #     [1,1,0,0,1],
    #     [1,1,0,1,0],
    #     [0,0,1,1,0],
    #     [0,1,0,1,0],
    #     [0,0,0,0,0],
    #     ]

    
    subsetofmatrixofones(M)