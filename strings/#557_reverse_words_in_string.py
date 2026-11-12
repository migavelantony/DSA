# LeetCode 557: Reverse Words in a String III
# Source: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# Problem summary (paraphrased):
# Reverse the characters within each word while keeping the word order and spaces in
# their original positions.

class Solution:

    def reverseWords(self, s: str) -> str:
        word = s.split()
        for i in range(len(word)):
            word[i] = word[i][::-1]
        return ' '.join(word)
