ls = [1,2,3,4,5]
target = 6

for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if i != ls[j]:
            if ls[i] + ls[j] == target:
                print(ls[i],ls[j])
    break



