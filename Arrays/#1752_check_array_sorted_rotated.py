# LeetCode 1752: Check if Array Is Sorted and Rotated
# Source: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
#
# Problem summary (paraphrased):
# Determine whether an array can be obtained by rotating a nondecreasing array,
# possibly by zero positions. Repeated values are allowed.

class Solution:

    def check(self, nums: list[int]) -> bool:
        decreasing = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                decreasing += 1
        if decreasing > 1:
            return False
        return True
