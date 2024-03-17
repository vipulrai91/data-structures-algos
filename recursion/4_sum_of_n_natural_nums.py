# shrink the input space after every call

num = 55


def sum_natural_num(num: int):
    # base case
    if num == 1:
        return num
    return num + sum_natural_num(num - 1)


print(sum_natural_num(num))
