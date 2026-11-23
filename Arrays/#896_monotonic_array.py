# LeetCode 896: Monotonic Array
# Source: https://leetcode.com/problems/monotonic-array/description/
#
# Problem summary (paraphrased):
# Determine whether the array never decreases or never increases. Equal neighboring
# values are allowed in either direction.

class Solution:

    def isMonotonic(self, nums: list[int]) -> bool:
        if nums[0] != max(nums):
            for i in range(1, len(nums)):
                if nums[i - 1] > nums[i]:
                    return False
        else:
            for i in range(1, len(nums)):
                if nums[i - 1] < nums[i]:
                    return False
        return True
