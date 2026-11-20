# LeetCode 1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
# Source: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
#
# Problem summary (paraphrased):
# Count the contiguous subarrays of exactly k elements whose average is at least the
# given threshold.

class Solution:

    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        avg = total / k
        count = 0
        if avg >= threshold:
            count += 1
        for i in range(k, len(arr)):
            total -= arr[i - k]
            total += arr[i]
            avg = total / k
            if avg >= threshold:
                count += 1
        return count
