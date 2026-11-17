# LeetCode 1342: Number of Steps to Reduce a Number to Zero
# Source: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
#
# Problem summary (paraphrased):
# Count the operations needed to reduce a nonnegative integer to zero: divide even
# values by two, and subtract one from odd values.

class Solution(object):

    def numberOfSteps(self, num):
        step = 0
        while num >= 1:
            if num % 2 == 0:
                num = num // 2
                step += 1
            else:
                num = num - 1
                step += 1
        return step
