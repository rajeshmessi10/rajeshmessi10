# #The Alternating Numbers
# In this challenge, you have to establish if an integer num is Alternating. To be Alternating, num must be positive and every digit in its sequence must have a different parity than its next and its previous digit.
#
# Given an integer num, implement a function that returns True is num is an Alternating number, or False if it's not.
# is_alternating(123) ➞ True
# # 1 is odd, 2 is even, 3 is odd
#
# is_alternating(67) ➞ True
# # 6 is even, 7 is odd
#
# is_alternating(2380) ➞ False
# # 2 is even, 3 is odd, 8 is even, 0 is even
#
# is_alternating(75) ➞ False
# 7 is odd, 5 is odd
def alternating_number(integer1):
    technique = []
    technique = ["even" if i % 2 == 0 else "odd" for i in range(1, len(str(integer1)) + 1)]
    new = [i for i in str(integer1)]
    for check in range(len(new)):
        if int(new[check]) % 2 == 1:
            new[check] = "odd"
        else:
            new[check] = "even"

    return technique == new
print(alternating_number(203))
print(alternating_number(12345))
print(alternating_number(67))