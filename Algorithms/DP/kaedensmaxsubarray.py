import sys
from sys import maxsize
def maxsubArray(arrayy, lengthh):

    currSum = 0
    MaxSum = -maxsize-1
    items = []
    for i in range(0,lengthh):
        currSum = currSum + arrayy[i]
        if currSum > MaxSum:
            items.append(arrayy[i])
            MaxSum = currSum
               

        if currSum < 0:
            currSum = 0
        
    print(MaxSum)
    print(items)

if __name__ == "__main__":
    a = [-2, -3, 4, -1, 2, 1, 5, -3] 
    maxsubArray(a,len(a))
