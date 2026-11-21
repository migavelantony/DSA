# LeetCode 1544: Make The String Great
# Source: https://leetcode.com/problems/make-the-string-great/description/
#
# Problem summary (paraphrased):
# Repeatedly remove neighboring letters that are the same letter in opposite cases.
# Return the string once no such pair remains.

class Solution(object):

    def makeGood(self, s):
        stack = []
        for ch in s:
            if stack and ch.lower() == stack[-1].lower() and (ch != stack[-1]):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
