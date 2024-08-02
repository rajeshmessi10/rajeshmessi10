l = ['m' , 'g' , 'g' , 'k' , 'I','g' , 'l',"u"]
k = {}
for i in l:
    if i in k:
        k[i] = k[i] + 1
    else:
        k[i] = 1


print(k)