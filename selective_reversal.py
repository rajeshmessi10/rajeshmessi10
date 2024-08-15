# Selective List Reversal
# Create a function that takes a list and a number and selectively reverse the order of the list based on the number you're given (second argument). If you're given the arguments [1,2,3,4,5,6] and 2, you would return the list [2,1, 4,3, 6,5].
#
# Examples
# sel_reverse([1,2,3,4,5,6], 2) ➞ [2,1, 4,3, 6,5]
#
# sel_reverse([2,4,6,8,10,12,14,16], 3) ➞ [6,4,2, 12,10,8, 16,14]
#
# sel_reverse([5,7,2,6,0,4,6], 100) ➞ [6,4,0,6,2,7,5]
# Notes
# If the list you're given can't be broken up into equal parts, just reverse the remaining numbers (see 2nd expample).
# If length exceeds the list length, reverse everything.
# If length is zero, return the original list.
def selective_reversal(lis , num):
    if num > len(lis):
        return lis[::-1]
    if num == 0:
        return lis
    new = []
    for ith in range(0, len(lis), num):
        new.extend(sorted(lis[ith:ith + num])[::-1])  # or  result.extend(lst[i:i + num][::-1])
    return new


print(selective_reversal([1,2,3,4,5,6], 2))