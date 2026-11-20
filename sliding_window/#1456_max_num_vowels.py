# LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length
# Source: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
#
# Problem summary (paraphrased):
# Among all substrings of length k, return the greatest count of lowercase vowels: a,
# e, i, o, and u.

class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        count = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            max_count = max(max_count, count)
        return max_count
