# Rearrange the Sentence
# Given a sentence with numbers representing a word's location embedded within each word, return the sorted sentence.
#
# Examples
# rearrange("is2 Thi1s T4est 3a") ➞ "This is a Test"
#
# rearrange("4of Fo1r pe6ople g3ood th5e the2") ➞ "For the good of the people"
#
# rearrange(" ") ➞ " "
# Notes
# Only the integers 1-9 will be used.
def rearrange_sentence(str1):
    final = ""
    new = []
    for ith in str1.split(" "):
        for jth in ith:
            if jth.isdigit():
                new.append(jth)
    for ith in sorted(new):
        for jth in str1.split(" "):
            if ith in jth:
                final += jth.replace(ith,"") + " "
    return final.strip()
print(rearrange_sentence("4of Fo1r pe6ople g3ood th5e the2"))