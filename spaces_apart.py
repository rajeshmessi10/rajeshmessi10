# Spaces Apart
# Create a function that takes an lst and returns the sum of the numbers between two "1"s.
#
# Examples
# space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]) ➞ 14
#
# space_apart(["1", 9, 20, 38, "1"]) ➞ 67

# space_apart([3, 2, 9, "1", 0, 0, -1, "1"]) ➞ "invalid"

def spaces_apart(lis):
    ranger = [i for i in range(len(lis)) if lis[i] == "1"]
    count = sum([lis[i] for i in range(ranger[0] + 1, ranger[1])])
    return count if count >= 0 else "invalid"

print(spaces_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]))
print(spaces_apart([3, 2, 9, "1", 0, 0, -1, "1"]))
