array = "kayak"
# array = "racecar"


# def palindrome(array):
#     # base case
#     if array == "":
#         return ""
#     return palindrome(array[1:]) + array[0]


# def check_palindrome(array):
#     if array == palindrome(array):
#         return True
#     return False


# print(check_palindrome(array))


# Pure recursive approach


def isPanlindrome(array):
    # base case

    if len(array) == 0 or len(array) == 1:
        return True

    if array[0] == array[-1]:
        return isPanlindrome(array[1:-1])

    return False


print(isPanlindrome(array))
