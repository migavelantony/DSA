# LeetCode 217: Contains Duplicate
# Source: https://leetcode.com/problems/contains-duplicate/description/
#
# Problem summary (paraphrased):
# Determine whether any value appears at least twice in the array.

class Solution(object):

    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
