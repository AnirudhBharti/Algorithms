listelem = []
def issubsetsum(set, n , sum):
    
    #Base cases
    if sum==0:
        print(listelem)
        return True
    if sum!=0 and n==0:
        return False
    
    if sum<set[n-1]:
        elem = issubsetsum(set,n-1,sum)
    else:
        elem = issubsetsum(set,n-1,sum) or issubsetsum(set,n-1,sum-set[n-1])
    
    listelem.append(set[n-1])
    return elem
      

if __name__ == "__main__":
    set = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(set)
    if (issubsetsum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")