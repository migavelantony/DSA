# LeetCode 167: Two Sum II - Input Array Is Sorted
# Source: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# Problem summary (paraphrased):
# Find two values in a sorted array that add to the target and return their one-based
# indices. There is exactly one solution; use constant extra space and do not reuse an
# element.

class Solution(object):

    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] == target:
                return [left + 1, right + 1]
