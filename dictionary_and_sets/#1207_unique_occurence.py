# LeetCode 1207: Unique Number of Occurrences
# Source: https://leetcode.com/problems/unique-number-of-occurrences/description/
#
# Problem summary (paraphrased):
# Check whether every distinct array value has a different occurrence count from every
# other distinct value.

class Solution:

    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        for i in arr:
            d[i] = d.get(i, 0) + 1
        return len(set(d.values())) == len(d)
