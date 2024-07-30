# Unique Character Mapping
# Write a function that returns a character mapping from a word.
#
# Examples
# character_mapping("abcd") ➞ [0, 1, 2, 3]
#
# character_mapping("abb") ➞ [0, 1, 1]
#
# character_mapping("babbcb") ➞ [0, 1, 0, 0, 2, 0]
#
# character_mapping("hmmmmm") ➞ [0, 1, 1, 1, 1, 1]
# Notes
# Start your counter at 0, and increment by 1 each time you encounter a new character.
# Identical characters should share the same number.

def unique_character_map(str1):
    new = {}
    final = []
    c = 0
    for i in range(len(str1)):
        if str1[i] in new:
            final.append(new[str1[i]])
            c += 1
        else:
            print(i , c)
            print(i-c)
            new[str1[i]] = i-c
            final.append(new[str1[i]])


    return final

print(unique_character_map("fluffy"))
