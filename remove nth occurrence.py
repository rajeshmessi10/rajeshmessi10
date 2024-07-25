# remove nth occurence

li = ["geeks" , "for" , "geeks" , "king"]
g = {}
c = 0

for i in li:
    g[i] =  c + g[i]


print(g)

