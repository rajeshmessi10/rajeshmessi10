import re

import re
def swap_x_y_coord_strings(str1):
    splitter = str1.split(")")
    print(splitter)
    new = []
    for ith in range(len(splitter)):
        tup = []
        numbers = re.findall(r'-?\d+',splitter[ith])
        append_tuple = [tup.append(int(i)) for i in numbers]
        if tup:
            new.append(tuple(tup[::-1]))
    return ", ".join([f"{str(i)}" for i in new])

print(swap_x_y_coord_string("(11, 23), (43, 99) , (67,90)"))