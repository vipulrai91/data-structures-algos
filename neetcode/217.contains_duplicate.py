# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        counter = {}

        for index, value in enumerate(nums):
            # print(index, value)
            if value in counter:
                return True
            else:
                counter.update({value: 1})

        return False


# nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]
nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


s = Solution()
print(s.containsDuplicate(nums=nums))
