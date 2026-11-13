# LeetCode 349: Intersection of Two Arrays
# Source: https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# Problem summary (paraphrased):
# Return the distinct values that occur in both input arrays, in any order.

class Solution(object):

    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
