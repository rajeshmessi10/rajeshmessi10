def pluralize(lis):
    dicti  = {}
    for word in lis:
        if word not in dicti:
            dicti[word] = 1
        else:
            dicti[word] =dicti[word] + 1
    return [i + "s" if dicti[i] > 1 else i for i in dicti]
print(pluralize(["chair", "pencil", "arm"]))