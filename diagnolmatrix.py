a = [[1,2,3,8],
       [4,5,6,0],
       [9,8,9,9]]
# 1 + 5 + 9 = 15 , 3+5+9 = 17 , 15-17 = 2
add1 = 0
add2 = 0
for row in range(0,len(a)):
    add1 += a[row][row]
    add2 += a[row][-row-1]
print(abs(add1 - add2))








