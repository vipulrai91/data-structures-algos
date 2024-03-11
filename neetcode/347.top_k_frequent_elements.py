# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1

        return counter


# nums = [1, 1, 1, 2, 2, 3]
nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums=nums, k=k))
