# LeetCode 387: First Unique Character in a String
# Source: https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# Problem summary (paraphrased):
# Find the index of the first character that occurs only once in the string. Return -1
# if every character repeats.

class Solution:

    def firstUniqChar(self, s: str) -> int:
        unique = {}
        for ch in s:
            unique[ch] = unique.get(ch, 0) + 1
        for i in range(len(s)):
            ch = s[i]
            if unique[ch] == 1:
                return i
        return -1
