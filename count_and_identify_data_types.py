# Count and Identify Data Types
# Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.
#
# List order is:
#
# [int, str, bool, list, tuple, dictionary]
# Examples
# count_datatypes(1, 45, "Hi", False) ➞ [2, 1, 1, 0, 0, 0]
#
# count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) ➞ [3, 0, 0, 1, 1, 0]
#
# count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) ➞ [2, 2, 3, 1, 0, 2]
#
# count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]) ➞ [2, 0, 1, 2, 2, 0]
# Notes
# If no arguments are given, return [0, 0, 0, 0, 0, 0]
def count_identify_datatype(*args):
    dic = {int : 0 , str: 0 , bool: 0 , list : 0 , tuple : 0 , dict:0}
    for i in args:
        if type(i) in dic:
            dic[type(i)] += 1
    return list(dic.values())
print(count_identify_datatype(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]))