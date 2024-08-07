# Highest Index (With a Twist)
# Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.
#
# Examples
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#
#
# alphabet_index(alphabet, "Flavio") ➞ "22v"
#
# alphabet_index(alphabet, "Andrey") ➞ "25y"
#
# alphabet_index(alphabet, "Oscar") ➞ "19s"
# Notes
# If you're stuck, check the Resources tab.
# sorted() is not best practice.

def highest_index(alpabhet , string_1):
    new = []
    for ith in string_1:
        if ith.lower() in alpabhet:
            new.append(alpabhet.index(ith.lower()) + 1)
        max = new[0]
        for jth in new:
            if jth >= max:
                max = jth
    return str(max) + alpabhet[max-1]
print(highest_index(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                                "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] , "Oscar"
))
