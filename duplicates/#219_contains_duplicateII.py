# LeetCode 219: Contains Duplicate II
# Source: https://leetcode.com/problems/contains-duplicate-ii/description/
#
# Problem summary (paraphrased):
# Determine whether two different indices contain the same value and are separated by
# at most k positions.

class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        last_seen = {}
        for i, number in enumerate(nums):
            if number in last_seen and i - last_seen[number] <= k:
                return True
            last_seen[number] = i
        return False
