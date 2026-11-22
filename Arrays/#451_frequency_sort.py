# LeetCode 451: Sort Characters By Frequency
# Source: https://leetcode.com/problems/sort-characters-by-frequency/description/
#
# Problem summary (paraphrased):
# Rearrange a string into contiguous groups of equal characters, placing more frequent
# characters first. Any ordering of equally frequent groups is valid.

class Solution:

    def frequencySort(self, s: str) -> str:
        freq = {}
        result = []
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for ch, count in ordered:
            result.append(ch * count)
        return ''.join(result)
