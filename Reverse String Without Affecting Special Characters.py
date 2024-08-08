def rev_specstring(s):
    # Create a list to hold the alphabetic characters in reverse order
    alpha_chars = [c for c in s if c.isalpha()]
    # Reverse the list of alphabetic characters
    alpha_chars.reverse()
    print(alpha_chars)
    # Create a list to hold the final characters
    result = []
    # Initialize an index for the reversed alphabetic characters
    alpha_index = 0
    # Iterate over the original string
    for c in s:
        if c.isalpha():
            # Place the next reversed alphabetic character
            result.append(alpha_chars[alpha_index])
            alpha_index += 1
        else:
            # Place the original special character or number
            result.append(c)
    # Join the list into a final string
    return ''.join(result)
# Test cases
print(rev_specstring("AFC#47GH$Ieu"))  # ➞ "ueI#47HG$CFA"
print(rev_specstring("guyhiuj1234!@#$%rtyhghu"))  # ➞ "uhghytr1234!@#$%juihyug"
print(rev_specstring("12!@"))  # ➞ "12!@"
