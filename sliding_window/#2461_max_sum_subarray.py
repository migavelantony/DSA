# LeetCode 2461: Maximum Sum of Distinct Subarrays With Length K
# Source: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
#
# Problem summary (paraphrased):
# Find the greatest sum among length-k contiguous subarrays whose elements are all
# distinct. Return zero if no such subarray exists.

class Solution:

    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        sub_array = {}
        total = 0
        max_sum = 0
        for i in range(k):
            num = nums[i]
            if num in sub_array:
                sub_array[num] += 1
            else:
                sub_array[num] = 1
            total += num
            if len(sub_array) == k:
                max_sum = total
        for i in range(k, len(nums)):
            outgoing = nums[i - k]
            sub_array[outgoing] -= 1
            if sub_array[outgoing] == 0:
                del sub_array[outgoing]
            num = nums[i]
            if num in sub_array:
                sub_array[num] += 1
            else:
                sub_array[num] = 1
            total -= outgoing
            total += num
            if len(sub_array) == k:
                max_sum = max(max_sum, total)
        return max_sum
