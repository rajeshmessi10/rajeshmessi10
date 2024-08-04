def list_summation(lis):
    if len(lis) == 0:
        return False
    return lis[0] + list_summation(lis[1:])


print(list_summation([1, 2, 3, 4, 10, 11]))


