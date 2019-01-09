def minimumcostmatrix(cost, m ,n):
    minMatrix=[[0 for i in range(3)] for j in range(4)]
    
    minMatrix[0][0] = cost[0][0]
    for p in range(1,m+1):
        minMatrix[p][0] = minMatrix[p-1][0]+cost[p][0]
    
    for q in range(1,n+1):
        minMatrix[0][q] = minMatrix[0][q-1]+cost[0][q]
    
    print(minMatrix)

    for x in range(1,m+1):
        for y in range(1,n+1):
            minMatrix[x][y] = cost[x][y]+min(minMatrix[x-1][y-1],minMatrix[x-1][y],minMatrix[x][y-1])

    print(minMatrix)

    return minMatrix[x][y]

if __name__ == "__main__":
    cost=[[3,2,8],
        [10,1,7],
        [10,5,2],
        [6,4,3]]
    
    print(minimumcostmatrix(cost,3,2))