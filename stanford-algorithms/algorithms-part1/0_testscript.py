import time


A = [1, 4, 5, 6, 3, 6, 10, 55]

t = 39


def check_occ(A, t):
    for index, val in enumerate(A):
        if val == t:
            print(f"Present at index {index - 1}")
            return True
    return False


# print(check_occ(A, t))


print(time.time_ns())

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


print(fact(3))
