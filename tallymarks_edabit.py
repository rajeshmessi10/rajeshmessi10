# Tally Marks
# Create a function that can convert from normal notation to tally-mark notation and vice versa. In tally-mark notation, a number can be decomposed as the sum of 5s + remainder.
#
# The function will look like this: switch_notation([current scores], desired notation)
#
# Ex.1 Normal: 3, 24, 4, 9
# Ex.1 Tally: 3, 55554, 4, 54
#
# Ex.2 Normal: 2, 12, 2, 4
# Ex.2 Tally: 2, 552, 2, 4


def switch_notation(lis , cond):
    if cond == "normal":
        new = [sum(int(i) for i in str(j)) for j in lis]
        return new
    else:
        final = []
        for ith in range(len(lis)):
            if lis[ith] < 5:
                final.append(lis[ith])
            else:
                val = ""
                c = 0
                for jth in range(1, lis[ith],5):
                    c+=5
                    if c <= lis[ith]:
                        val += "5"
                if lis[ith] % 5:
                    val += str((lis[ith] % 5))
                final.append(val)
        return [ int(i) for i in final]
print(switch_notation([3, 55,55551], "normal"))