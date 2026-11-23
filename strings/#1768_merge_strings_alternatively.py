# LeetCode 1768: Merge Strings Alternately
# Source: https://leetcode.com/problems/merge-strings-alternately/description/
#
# Problem summary (paraphrased):
# Build a string by taking one character from each input in turn, starting with the
# first input. Append the remaining suffix when either input runs out.

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return ''.join(result)
