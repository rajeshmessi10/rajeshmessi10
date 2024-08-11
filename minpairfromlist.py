# Input list
input_list = [3, 9, 50, 15, 99, 7, 98, 65]

# Sort the list
sorted_list = sorted(input_list)

# Initialize variables to track the minimum difference and the corresponding pair
min_diff = float('inf')
min_pair = []

# Iterate through the sorted list to find the pair with the smallest difference
for i in range(len(sorted_list) - 1):
    diff = sorted_list[i + 1] - sorted_list[i]
    if diff < min_diff:
        min_diff = diff
        min_pair = [sorted_list[i], sorted_list[i + 1]]

# Output the pair with the least difference
print(min_pair)
