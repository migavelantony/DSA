# LeetCode 1385: Find the Distance Value Between Two Arrays
# Source: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
#
# Problem summary (paraphrased):
# Count elements of the first array whose absolute difference from every element of the
# second array is greater than d.

class Solution(object):

    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for num1 in arr1:
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    break
            else:
                count += 1
        return count
