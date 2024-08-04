# Ones and Zeroes
# Write a function that returns True if every consecutive sequence of ones is followed by a consecutive sequence of zeroes of the same length.
#
# Examples
# same_length("110011100010") ➞ True
#
# same_length("101010110") ➞ False
#
# same_length("111100001100") ➞ True
#
# same_length("111") ➞ False
# Notes

str1 = "110011100010"
new , result_0 , length , final = [] , [] , [] , []
if '0' in str1:
    for ith in range(len(str1)):
        if str1[ith] == '0':
            result_0.append(str1[ith])
            if new:
                length.append(len(new))
            new.clear()
        else:
            new.append(str1[ith])
            if result_0:
                final.append(len(result_0))
                result_0.clear()
    if result_0:
        final.append(len(result_0))
    if final == length:
        print(True)
    else:
        print(False)
else:
    print("False")



