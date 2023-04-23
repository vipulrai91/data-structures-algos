# https://leetcode.com/problems/two-sum/
# All test cases success

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping_dict = {}
        for index, num in enumerate(nums):
            remainder = target - num
            if remainder in mapping_dict:
                return [mapping_dict[remainder], index]
            mapping_dict.update({num: index})


nums = [3, 2, 4]
target = 6
s = Solution()
print(s.twoSum(nums, target))
