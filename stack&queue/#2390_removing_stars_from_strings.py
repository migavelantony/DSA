# LeetCode 2390: Removing Stars From a String
# Source: https://leetcode.com/problems/removing-stars-from-a-string/description/
#
# Problem summary (paraphrased):
# For each star, delete that star and the nearest remaining non-star character to its
# left. Return the final string after every star is removed.

class Solution(object):

    def removeStars(self, s):
        stack = []
        for ch in s:
            if stack and ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
