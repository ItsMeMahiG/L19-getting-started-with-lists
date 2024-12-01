def word(mahilist) :
    c=0
    lst=[]
    for i in mahilist :
        if len (i)>1 and i[0]== i[-1]:
            c=c+1
            lst.append (i)
    print("list of words with its first and last character being the same\n",lst)
    return c

count=word(['swan','mom','dad','coconut'])
print("number of words having its first and last character being the same",count)
