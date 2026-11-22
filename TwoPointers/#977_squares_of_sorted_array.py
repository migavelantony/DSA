# LeetCode 977: Squares of a Sorted Array
# Source: https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# Problem summary (paraphrased):
# Square every value of a nondecreasing integer array and return the squares in
# nondecreasing order.

class Solution(object):

    def sortedSquares(self, nums):
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        position = len(nums) - 1
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                result[position] = left_square
                left += 1
            else:
                result[position] = right_square
                right -= 1
            position -= 1
        return result
