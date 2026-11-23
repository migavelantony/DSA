# LeetCode 80: Remove Duplicates from Sorted Array II
# Source: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
#
# Problem summary (paraphrased):
# Modify a sorted array in place so each distinct value appears at most twice,
# preserving order. Return the length of the resulting prefix using constant extra
# space.

class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        write = 0
        for num in nums:
            if write < 2 or num != nums[write - 2]:
                nums[write] = num
                write += 1
        return write
