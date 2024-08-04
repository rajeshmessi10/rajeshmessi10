def highest_occurrence(list1):
    dic = {}
    for val in list1:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 1
    a =  [key for key, value in dic.items() if value == max(dic.values())]

    return a

print(highest_occurrence(["it", "keeps", "coding", "on", "or", "it", "gets", "the", "hose"]))
