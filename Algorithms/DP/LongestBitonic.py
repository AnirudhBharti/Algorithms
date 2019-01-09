def LBS(nums):
    maxArray=[]
    minArray=[]
    n=len(nums)
    maxArray=[1 for x in range(n)]
    minArray=[1 for x in range(n)]
    
    result = 1
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                maxArray[i]=max(maxArray[i],maxArray[j]+1)

        result = max(maxArray[i], result)

    print(maxArray)

    result = 1
    for i in range(n-1,0,-1):
        for j in range(i):
            if nums[i]>nums[j]:
                minArray[i]=max(minArray[i],minArray[j]+1)

        result = max(minArray[i], result)

    print(minArray)

    value = maxArray[0]+minArray[0]-1
    for k in range(1, n):
        value = max(value, (maxArray[k]+minArray[k]-1))
    
    print(value)



if __name__ == "__main__":
    nums=[0 , 8 , 4, 12, 2, 10 , 6 , 14 , 1 , 9 , 5 , 13, 
        3, 11 , 7 , 15]
    LBS(nums)