def MaxGoldMine(Gold, m, n):
    G = []
    G = [[0 for x in range(n)] for y in range(m)]

    for col in range(n-1, -1, -1):
        for row in range(m):
            # right row
           
            if col == n-1:
                right = 0
            else:
                right = G[row][col+1]

            # right Up
           
            if row == 0 or col == n-1:
                rightUp = 0
            else:
                rightUp = G[row-1][col+1]

            # right Down
            
            if row == m-1 or col == n-1:
                rightDown = 0
            else:
                rightDown = G[row+1][col+1]

            G[row][col] = Gold[row][col]+max(right, rightUp, rightDown)
    
    print(G)
    # The max amount of gold 
    # collected will be the max 
    # value in first column of all rows 
    res = G[0][0] 
    for i in range(1, m): 
        res = max(res, G[i][0]) 

    print(res)

if __name__ == "__main__":
    Gold = [[1, 3, 1, 5],
            [2, 2, 4, 1],
            [5, 0, 2, 3],
            [0, 6, 1, 2]]
    MaxGoldMine(Gold, 4, 4)
