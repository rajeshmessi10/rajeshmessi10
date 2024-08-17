

def number_groups(a,b,c):
    new = set()
    for ith in a:
        if (ith in b) or (ith in c):
            new.add(ith)
    for jth in b:
        if (jth in a) or (jth in c):
            new.add(jth)
    for kth in c:
        if kth in a or kth in b: # is not required to check if a and b checks each on
            new.add(kth)
    return sorted(list(new))

print(number_groups([7, 8, 7,3, 4], [2, 9, 1, 2, 1], [5, 6, 11, 6, 5]))
print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]))
# [1,3]