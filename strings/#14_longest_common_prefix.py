# LeetCode 14: Longest Common Prefix
# Source: https://leetcode.com/problems/longest-common-prefix/description/
#
# Problem summary (paraphrased):
# Find the longest starting sequence shared by every string in the list. Return an
# empty string if they share no prefix.

class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        for position in range(len(strs[0])):
            expected = strs[0][position]
            for word in strs:
                if position >= len(word) or word[position] != expected:
                    return strs[0][:position]
        return strs[0]
