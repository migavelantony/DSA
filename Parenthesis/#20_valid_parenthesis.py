# LeetCode 20: Valid Parentheses
# Source: https://leetcode.com/problems/valid-parentheses/description/
#
# Problem summary (paraphrased):
# Check whether every opening bracket has a matching closing bracket of the same type
# in the correct nesting order. The possible bracket pairs are (), [], and {}.

class Solution(object):

    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
