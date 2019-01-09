def LIS(nums):
    maxArray=[]
    n=len(nums)
    maxArray=[1 for x in range(n)]
    
    result = 1
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                maxArray[i]=max(maxArray[i],maxArray[j]+1)

        result = max(maxArray[i], result)

    print(result)

if __name__ == "__main__":
    nums=[9,1,3,7,5,6,20]
    LIS(nums)