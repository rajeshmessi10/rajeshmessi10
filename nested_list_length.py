
def flatten(lis):
    new = []
    for i in lis:
        if isinstance(i, list):
            new.extend(flatten(i))  # recursively flatten a list by extending the current list new
        else:
            new.append(i)
    return new
flatt = flatten([1, [2], 1, [2], 1])
print(len(flatt))


