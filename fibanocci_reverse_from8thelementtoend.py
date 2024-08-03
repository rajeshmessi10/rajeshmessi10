# iccanobiF Numbers
# The Fibonacci sequence, as you know, is generated by iterative addition of the sum of the last two elements of the sequence to the end of the sequence, starting with [0, 1].
#
# Fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …]
# The iccanobiF sequence (see Resources tab for more info) is generated in a similar way — except that the digits of the last two elements should first be reversed, then added together, then added to the sequence. Single-digit numbers are unaffected, so the first 8 elements are identical to the Fibonacci sequence:

# iccanobiF = [0, 1, 1, 2, 3, 5, 8, 13]
# The next element is the sum of the reverse of 8 (still 8), and the reverse of 13 — 31 (8 + 31 = 39).
#
# iccanobiF = [0, 1, 1, 2, 3, 5, 8, 13, 39]
# The next element is 31 + 93 = 124
#
# iccanobiF = [0, 1, 1, 2, 3, 5, 8, 13, 39, 124]
# And so on.
#
# Create a function that takes a number n and returns the difference between the nth iccanobiF number and the nth Fibonacci number.
#
# Examples
# icc_minus_fib(4) ➞ 0
# # For all n < 9, the difference is zero.
#
# icc_minus_fib(9) ➞ 18
#
# icc_minus_fib(18) ➞ 790920
# Notes
# N/A


def fib_reversed(num):
    new = [0,1]
    org = [0,1]
    if num >= 9:
        for _ in range(num-2):
            if len(new) < 8:
                new.append(new[-1] + new[-2])
            else:
                new.append(int(str(new[-1])[::-1]) + int(str(new[-2])[::-1]))
        for _ in range(num - 2):
            org.append(org[-1] + org[-2])
        return new[-1] - org[-1]
    return 0
print(fib_reversed(49))

