
class QItem():
    def __init__(self, word, len):
        self.word=word
        self.len=len

def isAdjacent(a,b):
    count=0
    for i in range(len(a)):
        if(a[i]!=b[i]):
            count+=1
        if count > 1:
            return False
    print(count)
    return count==1

def wordladder(start, target, dictionary):
    print(start,target)
    print(dictionary)
    Q=[]
    Qit = QItem(start,1)
    print(Qit.word)
    Q.append(Qit)

    while(len(Q)>0):
        item = Q.pop()

        for d in dictionary:
            if isAdjacent(item.word, d) == True:
                temp = d
                QuuedItem = QItem(d, item.len+1)
                Q.append(QuuedItem)
                dictionary.remove(d)
                if temp==target:
                    return QuuedItem

if __name__=="__main__":
    dictionary = ["poon","plee","same","poie","plie","poin","plea"]
    start = "toon"
    target = "plea"
    returned = wordladder(start, target, dictionary)
    print(returned.word, returned.len)