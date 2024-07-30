# Replace With Next Largest Number
# Write a function that replaces each integer with the next largest in the list.
#
# Examples
# replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]
#
# replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]
#
# replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]
# Notes
# Replace the maximum with -1.
# Elements in the list will be unique.
# You don't have to swap the elements.
def replace_with_next_largest_number(lis):
    original_sort = sorted(lis)
    original_sort.append(-1)
    final = []
    for ith in range(len(lis)):
        if lis[ith] in original_sort:
            final.append(original_sort[original_sort.index(lis[ith]) + 1])
    return final
print(replace_with_next_largest_number([2, 3, 4, 5]))


# using list comprehension and can do with dictionary comprehension
def replace_with_next_largest_number(lis):
    original_sort = sorted(lis)
    original_sort.append(-1)
    return [original_sort[original_sort.index(lis[ith]) + 1] for ith in range(len(lis))]
print(replace_with_next_largest_number([2, 3, 4, 5]))






