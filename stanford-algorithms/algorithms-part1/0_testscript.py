A = [1, 4, 5, 6, 3, 6, 10, 55]

t = 39


def check_occ(A, t):
    for index, val in enumerate(A):
        if val == t:
            print(f"Present at index {index - 1}")
            return True
    return False


print(check_occ(A, t))
