def words(strng, dictionary):
   
    stringLen = len(strng)
    # if stringLen == 0:
    #     return True

    for i in range(1,stringLen+1):
        prefix = strng[0:i]
        if prefix in [value for (key,value) in dictionary.items() if value==prefix]:
           print(prefix)
           words(strng[i:stringLen],dictionary)
           return True
    
    return False
    
if __name__=="__main__":
    print('word break problem')
    dictionary = {"0":"pitch","1":"can","2":"candy","3":"rick","4":"joby","5":"smug","6":"a","7":"mass"}
    print(words('pitchcandymass',dictionary))