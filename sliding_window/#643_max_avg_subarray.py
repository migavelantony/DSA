# LeetCode 643: Maximum Average Subarray I
# Source: https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# Problem summary (paraphrased):
# Find the greatest average among all contiguous subarrays of exactly k elements.
# Answers within an absolute error of 0.00001 are accepted.

class Solution(object):

    def findMaxAverage(self, nums, k):
        total = sum(nums[:k])
        max_avg = float(total) / k
        for i in range(k, len(nums)):
            total -= nums[i - k]
            total += nums[i]
            avg = total / k
            if avg > max_avg:
                max_avg = avg
        return max_avg
