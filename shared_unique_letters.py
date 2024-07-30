# Shared vs. Unique Letters
# Create a function that takes in two words as input and returns a list of three elements, in the following order:

# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element should have unique letters, and have each letter be alphabetically sorted.
#
# Examples
# letters("sharp", "soap") ➞ ["aps", "hr", "o"]
#
# letters("board", "bored") ➞ ["bdor", "a", "e"]
#
# letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
#
# letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# # Even with multiple matching letters (e.g. 3 f's), there should
# # only exist a single "f" in your first element.
#
# letters("match", "ham") ➞ ["ahm", "ct", ""]
# # "ham" does not contain any letters that are not found already
# # in "match".
# Notes
# Both words will be in lower case.
# You do not have to worry about punctuation, all words only have letters from [a-z].
# If an element contains no letters, return an empty string (see last example).
def shared_unique(word1 , word2):
    final_list = []
    w = ""
    for ith in word1:
        if ith in word2:
            w+=ith
    final_list.append(w)
    w = ""
    for ith in word1:
        if ith not in word2:
            w+=ith
    final_list.append(w)
    w = ""
    for ith in word2:
        if ith not in word1:
            w+=ith
    final_list.append(w)
    return final_list
print(shared_unique("sharp" , "soap"))
