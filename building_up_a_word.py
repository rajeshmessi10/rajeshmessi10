def building_up_a_word(list_of_words):
    for ith in range(len(list_of_words)-1):
        if list_of_words[ith] not in list_of_words[ith+1]:
            return False
        elif len(list_of_words[ith+1]) - len(list_of_words[ith]) > 1:
            return False
    return True
print(building_up_a_word(["a", "at", "ate", "late", "plate", "plater", "platter"]))