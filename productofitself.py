def product_of_itself_in_list(lis):
    final = []
    new = [i for i in lis]
    for ith in lis:
        prod = 1
        for jth in new:
            if jth != ith:
                prod *= jth
        final.append(prod)
    return final


print(product_of_itself_in_list([1, 2, 3, 4, 5, 6]))


# chatgpt way
def product_of_itself_in_list(lis):
    total_prod = 1
    for num in lis:
        total_prod *= num

    return [total_prod // num for num in lis]


# Test the function
print(product_of_itself_in_list([1, 2, 3, 4, 5, 6]))
