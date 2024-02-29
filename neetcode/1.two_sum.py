# Given an array of integers nums and an integer target, return indices of the two numbers such
# that they add up to target.

# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.

# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        counter = {}
        for idx, val in enumerate(nums):
            print(idx, val)
            diff = target - val
            if diff in counter:
                return [idx, counter[diff]]
            counter[val] = idx


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums=nums, target=target))
