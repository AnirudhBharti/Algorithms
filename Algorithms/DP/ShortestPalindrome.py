
def isPalindrome(str, st, end):
    while(st < end):
        if(str[st] != str[end]):
            return False
        st += 1
        end -= 1

    return True


def MinimimCount(str):
    n = len(str)

    count = 0
    flag = 0

    for i in range(n-1, -1, -1):
        if(isPalindrome(str, 0, i)):
            flag = 1
            break
        else:
            count+=1
    if flag == 1:
        return count

if __name__ == "__main__":
   print(MinimimCount("JAVA"))
