# LeetCode 1732: Find the Highest Altitude
# Source: https://leetcode.com/problems/find-the-highest-altitude/description/
#
# Problem summary (paraphrased):
# Starting at altitude zero, return the highest altitude reached after applying the
# successive altitude gains.

class Solution(object):

    def largestAltitude(self, gain):
        current = 0
        highest = 0
        for g in gain:
            current = current + g
            highest = max(highest, current)
        return highest
