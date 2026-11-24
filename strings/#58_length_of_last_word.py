# LeetCode 58: Length of Last Word
# Source: https://leetcode.com/problems/length-of-last-word/description/
#
# Problem summary (paraphrased):
# Count the characters in the last word, ignoring trailing spaces.

class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length
