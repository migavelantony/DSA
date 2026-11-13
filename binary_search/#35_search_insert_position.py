# LeetCode 35: Search Insert Position
# Source: https://leetcode.com/problems/search-insert-position/description/
#
# Problem summary (paraphrased):
# For a sorted array of distinct values, return the target's index if present, or the
# index where it should be inserted to preserve sorting. Use logarithmic time.

class Solution:

    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return left
