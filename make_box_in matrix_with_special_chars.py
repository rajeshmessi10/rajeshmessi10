# Making a Box 2.0!
# This is based on Helen Yu's Making a Box challenge. This challenge is the same execpt that instead of a list of strings, your function should output a matrix of characters.
#
# Examples
# char_box(1) ➞ [
#   ["#"]
# ]
#
# char_box(4) ➞ [
#   ["#", "#", "#", "#"],
#   ["#", " ", " ", "#"],
#   ["#", " ", " ", "#"],
#   ["#", "#", "#", "#"]
# ]

# char_box(2) ➞ [
#   ["#", "#"],
#   ["#", "#"]
# ]
# Notes
# As an added bonus, try making char_box(0) output [[]] and make any strings, non-integers, and negative numbers output -1.
from pprint import pprint
def make_box(num):
    matrix = [["*" for _ in range(0,num * num , num)] for _ in range(num)]
    for ith in range(1,len(matrix[0])-1):
        for jth in range(1, len(matrix[0])-1):
            matrix[ith][jth] = " "
    return matrix
pprint(make_box(1))