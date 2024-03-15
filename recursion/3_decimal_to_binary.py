num = 233


def findBinary(decimal: int, result: str = ""):
    if decimal == 0:
        return result

    result = str(decimal % 2) + result
    return findBinary(decimal // 2, result)  # operator //  is floor division


print(findBinary(num))
