# https://www.youtube.com/watch?v=4acikH5mXwk

##  Base case 0 or 1 since this is recursive
## break in the original list

# import numpy as np
# A = np.random.randint(100, size=10)

A = [91, 80, 35, 69, 41, 91, 7, 74, 78, 61]

print(A)


def merge(left, right):
    pass


def merge_sort(inputarray: list):
    # base case
    array_len = len(inputarray)

    if array_len <= 1:
        return inputarray

    # divide the array in half
    half = inputarray // 2
    left = merge_sort(inputarray[:half])
    right = merge_sort(inputarray[half:])
    return merge(left, right)
