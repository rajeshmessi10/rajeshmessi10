# Identical Row and Column?
# Write a function that returns True if there exists a row that is identical to a column in a 2-D matrix, otherwise False.
#
# To illustrate:
#
# [
#   [1, 2, 3, 4],
#   [2, 4, 9, 8],
#   [5, 9, 7, 7],
#   [6, 8, 1, 0]
# ]
#
# # 2nd row + 2nd column are identical: [2, 4, 9, 8]

def identical_row_col(lis):
    for row in range(len(lis)):
        new = []
        for col in range(len(lis[row])):
            new.append(lis[col][row])
        if new in lis:
            return True
    return False
print(identical_row_col([
[1, 2, 3, 4],
  [2, 4, 9, 8],
  [5, 9, 7, 7],
  [6, 8, 1, 0]
]))