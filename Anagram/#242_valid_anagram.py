# LeetCode 242: Valid Anagram
# Source: https://leetcode.com/problems/valid-anagram/description/
#
# Problem summary (paraphrased):
# Decide whether two strings contain exactly the same characters with the same counts.

class Solution(object):

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s_seen = {}
        t_seen = {}
        for ch in s:
            if ch in s_seen:
                s_seen[ch] += 1
            else:
                s_seen[ch] = 1
        for ch in t:
            if ch in t_seen:
                t_seen[ch] += 1
            else:
                t_seen[ch] = 1
        if s_seen == t_seen:
            return True
        else:
            return False
