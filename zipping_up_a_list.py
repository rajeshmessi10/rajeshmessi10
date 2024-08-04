# Zipping Up a List
# Two lists are part of the same zipper if the ending is identical. The identical section can be thought of as being "zipped-up". Below, [2, 2, 4] is "zipped-up".
#
# List 1: [3, 5, 8, 9, 2, 2, 4]
# List 2: [1, 7, 2, 2, 4]
# Create a function that takes in two lists. Return False if none of the list is "zipped." Return True if the lists are identical. Otherwise, return a list with the first index in each list where the zipper diverges.
#
# To illustrate:
#
# zipper([3, 5, 8, 9, 2, 2, 4], [1, 7, 2, 2, 4]) ➞ [3, 1]
# # Zipper 1: 9 (index-3) is first element to diverge.
# # Zipper 2: 7 (index-1) is first element to diverge.
# Examples
# zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]) ➞ [4, 7]
#
# zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]) ➞ [0, 0]
#
# zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]) ➞ False
#
# zipper([5, 4, 3, 2, 6], [5, 4, 3, 2, 6]) ➞ True
def zipping_list_end(list1 , list2):
    new = []
    if list1 == list2:
        return True
    for ith in range(-1,-len(list1)-1,-1):
        if list1[ith] != list2[ith]:
            if list1[ith] == list2[ith]:
                pass
            else:
                new.append(len(list1) - (-ith))
                new.append(len(list2) - (-ith))
                break
            return False
    return new
print(zipping_list_end([5, 5, 7, 8, 9, 1, 2],  [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]))