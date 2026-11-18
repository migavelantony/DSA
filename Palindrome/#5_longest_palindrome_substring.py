# LeetCode 5: Longest Palindromic Substring
# Source: https://leetcode.com/problems/longest-palindromic-substring/description/
#
# Problem summary (paraphrased):
# Find a longest contiguous part of the string that reads identically forward and
# backward.

class Solution(object):

    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        start = 0
        end = 0
        for i in range(len(s)):
            left, right = (i, i)
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                if right - left > end - start:
                    start = left
                    end = right
                left -= 1
                right += 1
            left, right = (i, i + 1)
            while left >= 0 and right < len(s) and (s[left] == s[right]):
                if right - left > end - start:
                    start = left
                    end = right
                left -= 1
                right += 1
        return s[start:end + 1]
