#abc,acb ,bca ,cba ,bac,cab
# bac , cba , acb , bca , cab ,abc
def pc(str1):

    new = [] # list for first appraoch
    m = [] # list to reverse string and append
    st = ""
    lis = list(str1)
    for i in range(0,len(str1)):
        for j in  range(i + 1 , len(str1)):
            lis[i] , lis[j] = lis[j] , lis[i]
            new.append("".join(lis))
            m.append("".join(lis[::-1]))
            lis = list(str1)


    return new + m
print(pc("abc"))










