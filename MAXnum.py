# bruteforce attack

arr = [31,7,29,9,5,17,23]
m = arr[0]
def mx(arr):
    m = arr[0]
    for i in range(0,len(arr)):
        if arr[i] >= m:
            m = arr[i]
    return m
print(mx([31,7,29,9,5,17,23,999,23,4,2]))

