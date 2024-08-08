# Split String by Identical Characters
# Create a function that splits a string into an array of identical clusters.
#
# Examples
# split_groups("555") ➞ ["555"]
#
# split_groups("5556667788") ➞ ["555", "666", "77", "88"]
#
# split_groups("aaabbbaabbab") ➞ ["aaa", "bbb", "aa", "bb", "a", "b"]
#
# split_groups("abbbcc88999&&!!!_") ➞ ["a", "bbb", "cc", "88", "999", "&&", "!!!", "_"]
# Notes
# Each cluster should only have one unique character.
# The resulting array should be in the same order as the input string.
# Should work with letters, numbers and other characters.
def split_by_identical(strings):
    new = []
    word = "" + strings[0]
    for ith in range(1,len(strings)):
        if strings[ith] in word:
            word += strings[ith]
        else:
            new.append(word)
            word = strings[ith]
    new.append(word)
    return new
print(split_by_identical("abbbcc88999&&!!!_"))