def fact(num):
    fact = 1
    if num <=1:
        return "fact is 1"
    else:
        for i in range(1,num+1):
            fact*=i # fact = fact * i
    return fact

print(fact(7))