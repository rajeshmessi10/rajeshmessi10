

for num in range(2,10):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print("its prime", num)

num = int(input("Enter a number: "))

for i in range(2, num + 1):
    for j in range(2, num + 1):
        if i % j == 0:
            break
    if i == j:
        print(i, end=',')


num = 40
l = []

for i in range(1,num+1):
    if num % i == 0:
        l.append(i)
        print(i)

if len(l) == 2:
    print(num , "is prime")


for j in range(2,101):
    for i in range(2,j):
        if j % i == 0:
            break
    else:
        print(j , end = "")
