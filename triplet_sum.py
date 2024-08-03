def triplet_sum(lis,val):
    con = set()
    if len(lis) >= 3:
        for ith in range(len(lis)):
            for jth in range(ith + 1, len(lis)):
                for wth in range(jth + 1, len(lis)):
                    if lis[ith] + lis[jth] + lis[wth] == val:
                        con.add((lis[ith], lis[jth], lis[wth]))
        return len(con)
    return False
print(triplet_sum([1, 2, 6, 3, 4, 5, 9, 10, 11], 20))
def triplet_sum(lst, val):
    lst.sort()
    triplets = set()
    print(lst)
    for i in range(len(lst) - 2):
        left, right = i + 1, len(lst) - 1
        while left < right:
            current_sum = lst[i] + lst[left] + lst[right]
            print(lst[i] , lst[left] , lst[right])
            if current_sum == val:
                triplets.add((lst[i], lst[left], lst[right]))
                left += 1
                right -= 1
            elif current_sum < val:
                left += 1
            else:
                right -= 1
    return len(triplets)
print(triplet_sum([1, 2, 6, 3, 4, 5, 9, 10, 11], 20))



