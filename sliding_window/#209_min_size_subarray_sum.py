# LeetCode 209: Minimum Size Subarray Sum
# Source: https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# Problem summary (paraphrased):
# For a positive-integer array and positive target, find the shortest contiguous
# subarray whose sum reaches or exceeds the target. Return zero if none exists.

class Solution:

    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total_sum = sum(nums)
        if total_sum < target:
            return 0
        total = 0
        left = 0
        min_length = float('inf')
        for i in range(len(nums)):
            if nums[i] >= target:
                return 1
            total += nums[i]
            while total >= target:
                widow_length = i - left + 1
                min_length = min(min_length, widow_length)
                total -= nums[left]
                left += 1
        return min_length
