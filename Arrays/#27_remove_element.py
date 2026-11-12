# LeetCode 27: Remove Element
# Source: https://leetcode.com/problems/remove-element/description/
#
# Problem summary (paraphrased):
# Remove every occurrence of a target value from an array in place. Return the number
# of retained elements and place those elements in the first part of the array; their
# order may change.

class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1
        return left
