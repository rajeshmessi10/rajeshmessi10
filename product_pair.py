# A Product Pair
# Mubashir needs your help in a simple task of multiplication of elements in a given list.
#
# Create a function which takes a list of integers lst and a positive integer k and returns the minimum and maximum possible product of k elements taken from the list. If enough elements are not available in the list, return None.
#
# Examples
# product_pair([1, -2, -3, 4, 6, 7], 1) ➞ (-3, 7)
#
# product_pair([1, -2, -3, 4, 6, 7], 2) ➞ (-21, 42)
# # -3*7, 6*7
#
# product_pair([1, -2, -3, 4, 6, 7], 3) ➞ (-126, 168)
# # -3*6*7, 4*6*7
#
# product_pair([1, -2, -3, 4, 6, 7], 7) ➞ None
# # There are only 6 elements in the list
# Notes
# N/A
def product_pair(lst , integer_1):
    final_list = []
    sorted_list = sorted(lst)
    val = sorted_list[0]
    val1 = 1
    for ith in range(1,integer_1):
        val *= sorted_list[-ith]
    for jth in range(1,integer_1+1):
        val1 *= sorted_list[-jth]
    return (val , val1)
print(product_pair([1, -2, -3, 4, 6, 7] , 3))