# LeetCode 1: Two Sum
# Source: https://leetcode.com/problems/two-sum/description/
#
# Problem summary (paraphrased):
# Find the indices of two different array elements whose values add to the target.
# Exactly one pair is guaranteed; either index order is acceptable.

class Solution(object):

    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[num] = i
