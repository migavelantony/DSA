# LeetCode 1480: Running Sum of 1d Array
# Source: https://leetcode.com/problems/running-sum-of-1d-array/description/
#
# Problem summary (paraphrased):
# Build an array whose entry at each index is the sum of all input values from the
# beginning through that index.

class Solution(object):

    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums
