import sys
def mincostmatrix(cost,m,n):
    if n<0 or m<0:
        return sys.maxsize 
   
    elif m==0 and n==0:
        return cost[m][n]

    else:
        return min(mincostmatrix(cost,m-1,n-1),mincostmatrix(cost,m-1,n),mincostmatrix(cost,m,n-1))+cost[m][n]

def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        return sys.maxsize 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    
    return cost[m][n] + min(minCost(cost, m-1, n-1), 
                                minCost(cost, m-1, n), 
                                minCost(cost, m, n-1)) 

if __name__ == "__main__":
    cost=[[3,2,8],
        [10,9,7],
        [10,5,2],
        [6,4,3]]
    print(cost)
    print(minCost(cost,3,1))