# Rhyme Time
# Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
#
# Examples
# does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True
#
# does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# # Capitalization and punctuation should not matter.
#
# does_rhyme("You are off to the races", "a splendid day.") ➞ False
#
# does_rhyme("and frequently do?", "you gotta move.") ➞ False
# Notes
# Case insensitive.
# Here we are disregarding cases like "thyme" and "lime".
# We are also disregarding cases like "away" and "today" (which technically rhyme, even though they contain different vowels).
def rhyme(str1 , str2):
    new = ""
    length = min(len(str1) , len(str2))
    for ith in range(-1 , -length-1,-1):
        if str1[ith] == " ":
            break
        else:
            if not str1[ith] in ['i' , '!' , '?']:
                new += str1[ith]
    print(new[::-1])
    last_word = str2.split(" ")[-1].strip(".,!,?")
    if last_word.islower():
        if new[::-1].lower() in last_word:
            return True
    if last_word.isupper():
        if new[::-1].upper() in last_word:
            return True
    return False
print(rhyme("and frequently do?", "you gotta move."))


