# LeetCode 1047: Remove All Adjacent Duplicates In String
# Source: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# Problem summary (paraphrased):
# Repeatedly delete a pair of equal neighboring characters until no such pair remains.
# Return the resulting string.

class Solution(object):

    def removeDuplicates(self, s):
        stack = []
        for ch in s:
            if stack and ch == stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
