# Write a funtion that takes in a non empty array of integers that are sorted in ascending order
# and returns a new array of the same length with the squares of original intergers also sorted
# in ascending order


# Sample input
array = [1, 2, 3, 4, 5, 6, 8, 9]
sample_op = [1, 4, 9, 16, 25, 36, 64, 81]


class SortedArraySquare:
    def __init__(self, array) -> None:
        self.array = array
        self.sorted_result = self.sortedsquare()

    def sortedsquare(self):
        return sorted([x * x for x in self.array])


sa = SortedArraySquare(array)
print(sa.sorted_result)
