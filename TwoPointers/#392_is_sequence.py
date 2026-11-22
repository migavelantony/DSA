# LeetCode 392: Is Subsequence
# Source: https://leetcode.com/problems/is-subsequence/description/
#
# Problem summary (paraphrased):
# Decide whether the first string can be obtained from the second by deleting zero or
# more characters without changing the order of those retained.

class Solution(object):

    def isSubsequence(self, s, t):
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1
                if right == len(t):
                    return False
        return left == len(s)
