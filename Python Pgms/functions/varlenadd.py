def add_num(*vars):
    sum = 0
    for num in vars:
        sum += num
    return sum


print(add_num(1, 2, 3))
