# Letters Formed from the Longest Word
# Write a function that returns True if all the strings in a list can be formed by using only the characters from the longest string.
#
# Examples
# can_form(["mast", "manifest", "met", "fan"]) ➞ True
#
# can_form(["may", "master", "same", "reams"]) ➞ False
#
# can_form(["may", "same", "reams", "mastery"]) ➞ True

def Letters_Formed_from_the_Longest_Word(list_of_words):
    new = []
    for ith in range(len(list_of_words)):
        word = ""
        if list_of_words[ith] != max(list_of_words , key = len):
            for jth in list_of_words[ith]:
                if jth in max(list_of_words , key = len):
                    word += jth
                else:
                    return False
            if word == list_of_words[ith]:
                new.append(True)
    return all(new)
print(Letters_Formed_from_the_Longest_Word(["may", "same", "reams", "mastery"]))
