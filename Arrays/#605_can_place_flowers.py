# LeetCode 605: Can Place Flowers
# Source: https://leetcode.com/problems/can-place-flowers/description/
#
# Problem summary (paraphrased):
# Given a valid row of occupied and empty planting spots, determine whether n
# additional flowers fit without any two flowers occupying neighboring spots.

class Solution:

    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
        return n <= 0
