# LeetCode 704: Binary Search
# Source: https://leetcode.com/problems/binary-search/description/
#
# Problem summary (paraphrased):
# Find a target in an ascending sorted integer array using logarithmic time. Return its
# index, or -1 if absent.

class Solution:

    def search(self, nums: list[int], target: int) -> int:
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
        return -1
