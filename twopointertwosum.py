#works only when list is sorted in ascending order
def two_sum(arr, target):
    pointer_one = 0
    pointer_two = len(arr) - 1

    while pointer_one < pointer_two:
        sum = arr[pointer_one] + arr[pointer_two]

        if sum == target:
            return pointer_one, pointer_two
        elif sum < target:
            pointer_one += 1
        else:
            pointer_two -= 1

    return False

print(two_sum([1 , 3, 4, 8, 9], 7))