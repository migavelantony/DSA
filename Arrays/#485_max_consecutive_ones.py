# LeetCode 485: Max Consecutive Ones
# Source: https://leetcode.com/problems/max-consecutive-ones/description/
#
# Problem summary (paraphrased):
# Return the longest consecutive run of ones in a binary array.

class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        left = 0
        right = 0
        longest = 0
        while right < len(nums):
            if nums[right] == 1:
                longest = max(longest, right - left + 1)
                right += 1
            else:
                right += 1
                left = right
        return longest
