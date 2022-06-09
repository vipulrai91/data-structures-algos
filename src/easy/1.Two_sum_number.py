# Given an array of distinct integers and an integer representing the target sum, we are asked to
#  implement a function that is going to find out whether there's a pair of numbers in the array
#  that adds up to the target sum. If such pair exists, return the pair in any order;
# otherwise return an empty array. We cannot add a number to itself to get the target sum.


# Sample input
from operator import indexOf


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10


class TwoSum:
    def __init__(self, array, targetSum) -> None:
        self.array = array
        self.targetSum = targetSum

    def two_sum(self) -> list:
        prevMap = {}

        for index, val in enumerate(self.array):
            diff = self.targetSum - val
            if diff in prevMap.keys():
                return [diff,val]
            prevMap.update({val: index})
        return []


ts = TwoSum(array=array, targetSum=targetSum)
print(ts.two_sum())
