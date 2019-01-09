# A Dynamic Programming solution for subset sum problem
# Returns true if there is a subset of
# set[] with sun equal to given sum

# Returns true if there is a subset of set[]
# with sun equal to given sum


def isSubsetSum(set, n, sum):

    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum+1)]
               for i in range(n+1)])

    # If sum is 0, then answer is true
    for i in range(n+1):
        subset[i][0] = True

        # If sum is not 0 and set is empty,
        # then answer is false
        for i in range(1, sum+1):
            subset[0][i] = False

        # Fill the subset table in botton up manner
        for i in range(1, n+1):
            for j in range(1, sum+1):
                if j < set[i-1]:
                    subset[i][j] = subset[i-1][j]
                if j >= set[i-1]:
                    subset[i][j] = (subset[i-1][j] or
                                    subset[i - 1][j-set[i-1]])

        # uncomment this code to print table
        # for i in range(n+1):
        # for j in range(sum+1):
        #	 print (subset[i][j],end=" ")
        # print()

    p = n
    q = sum
    m = sum

    listelements = []

    # Back tracking for printing elements of subset contributing to a sum
    index = p-1
    if(subset[p][q] == True):
        while(sum != 0):
            currentElem = set[index]
            if(subset[p-1][q] == False):
                sum = sum-currentElem
                q = sum
                listelements.append(currentElem)
            else:
                p = p-1
                index = index-1
                q = sum

    print('solution')
    print(listelements)

    return subset[n][m]


# Driver program to test above function
if __name__ == '__main__':
    set = [1, 3, 9, 2]
    sum = 12
    n = len(set)
    if (isSubsetSum(set, n, sum) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")

# This code is contributed by
# sahil shelangia.
