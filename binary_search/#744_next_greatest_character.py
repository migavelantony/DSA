# LeetCode 744: Find Smallest Letter Greater Than Target
# Source: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# Problem summary (paraphrased):
# From a sorted character array, return the smallest letter strictly greater than the
# target. If none exists, wrap around and return the first letter.

class Solution:

    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            if letters[middle] > target:
                right = middle - 1
            elif letters[middle] < target:
                left = middle + 1
            else:
                left = middle + 1
        if left < len(letters):
            return letters[left]
        return letters[0]
