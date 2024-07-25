# "aaaabbbccrttt" output: a5b3c2

a = "aaaabbbccrtt"

d = {}

for i in a:
    if i in d:
        d[i] += 1

    else:
        d[i] =1

print("".join([a + str(i) for a,i in d.items()]))




