a = [1, 2, 3, 4, 5, 6]
# [6,5,4,3,2,1]
# to reverse and replace elements in list
for ith in range(len(a) // 2):  # div the list to half and replace each other
    a[ith], a[len(a) - ith - 1] = a[len(a) - ith - 1], a[ith]
print(a)
# to get max value and key in dictionary
dic = {1: 2, 3: 56, 7: 90, 0: 88, 4: 456, 8: 9087}
print(max(dic, key=dic.get))
print(max(dic.values()))
# print from reverse angle of list or range of numbers
for it in range(11, -1, -1):
    print(it)
# isinstance check type for data type
print(isinstance(10, int))


# to flatten a list
def flatten(lis):
    new = []
    for value in lis:
        if isinstance(value, list):
            new.extend(flatten(value))
        else:
            new.append(value)
    return new


print(flatten([1, 2, [3, 4, [5, 6]], 7, 8]))

# add tuple
t = (1,2,3,4,45,6,)
print(t+(5,6,7,8))



