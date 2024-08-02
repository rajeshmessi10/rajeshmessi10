import re
def sum_of_negative_numbers(str1):
    find_all = re.findall(r'-\d+' , str1)

    return sum([int(num) for num in find_all])



print(sum_of_negative_numbers("22 13%14&-11-22 13 12"))
