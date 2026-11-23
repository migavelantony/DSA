# LeetCode 724: Find Pivot Index
# Source: https://leetcode.com/problems/find-pivot-index/description/
#
# Problem summary (paraphrased):
# Return the earliest index whose preceding values and following values have equal
# sums. An empty side has sum zero; return -1 if no index qualifies.

class Solution:

    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1
