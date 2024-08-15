# Add up to Even Number with Primes
# Create a function that takes an even number (will always be greater than 4) and return a list of all pairs of prime numbers which add up to the given number.
#
# Examples
# prime_pair_list(10) ➞ ["3+7", "5+5"]
#
# prime_pair_list(50) ➞ ["3+47", "7+43", "13+37", "19+31"]
#
# prime_pair_list(100) ➞ ["3+97", "11+89", "17+83", "29+71", "41+59", "47+53"]
def add_upto_prime(num):
    prime = []
    final = []
    for ith in range(2, num):
        for jth in range(2, ith):
            if ith % jth == 0:
                break
        else:
            prime.append(ith)
    for ith in range(len(prime)):
        for jth in range(ith+1 , len(prime)):
            if prime[ith] + prime[jth] == num:
                final.append(f"{prime[ith]} + {prime[jth]}")
    return final

print(add_upto_prime(100))

