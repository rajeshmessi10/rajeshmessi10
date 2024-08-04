def beginning_end(lis):
    new =[]
    for ith in range(len(lis)//2 +1):
        new.append([lis[ith] , lis[len(lis)-ith-1]])
    return new

print(beginning_end([5, 9, 8, 1, 2]))

print(beginning_end([1, 2, 3, 4, 5, 6, 7]))
