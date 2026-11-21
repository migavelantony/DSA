# LeetCode 56: Merge Intervals
# Source: https://leetcode.com/problems/merge-intervals/description/
#
# Problem summary (paraphrased):
# Combine every overlapping pair of intervals and return the resulting non-overlapping
# intervals covering the same values.

class Solution:

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged = []
        merged.append(intervals[0])
        for i in range(1, len(intervals)):
            existing_start, existing_end = merged[-1]
            incoming_start, incoming_end = intervals[i]
            if incoming_start > existing_end:
                merged.append([incoming_start, incoming_end])
            else:
                combined_end = max(existing_end, incoming_end)
                merged[-1] = [existing_start, combined_end]
        return merged
