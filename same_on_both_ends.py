# Same on Both Ends
# Given a sentence, return the number of words which have the same first and last letter.
#
# Examples
# count_same_ends("Pop! goes the balloon") ➞ 1
#
# count_same_ends("And the crowd goes wild!") ➞ 0
#
# count_same_ends("No I am not in a gang.") ➞ 1
# Notes
# Don't count single character words (such as "I" and "A" in example #3).
# The function should not be case sensitive, meaning a capital "P" should match with a lowercase one.
# Mind the punctuation!
# Bonus points indeed for using regex!

def same_on_both_ends(strings1):
    cnt = 0
    for ith in strings1.split(" "):
        s = "".join([jth for jth in ith if jth.isalpha()])
        if len(s) > 1 and s[0].lower() == s[-1].lower():
            cnt += 1
    return cnt
print(same_on_both_ends("Pop! goes the balloon!."))