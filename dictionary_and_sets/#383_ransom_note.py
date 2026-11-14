# LeetCode 383: Ransom Note
# Source: https://leetcode.com/problems/ransom-note/description/
#
# Problem summary (paraphrased):
# Determine whether the ransom-note string can be assembled from the magazine string.
# Each character occurrence from the magazine may be used at most once.

class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1
        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1
        return True
