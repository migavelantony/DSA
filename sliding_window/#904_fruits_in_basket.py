# LeetCode 904: Fruit Into Baskets
# Source: https://leetcode.com/problems/fruit-into-baskets/description/
#
# Problem summary (paraphrased):
# Choose the longest contiguous run of trees containing at most two fruit types.
# Starting anywhere, collect one fruit from each successive tree until a third type
# prevents continuing.

class Solution:

    def totalFruit(self, fruits: list[int]) -> int:
        basket = {}
        max_count = 0
        left = 0
        count = 0
        for i in range(len(fruits)):
            fruit = fruits[i]
            basket[fruit] = basket.get(fruit, 0) + 1
            while len(basket) > 2:
                outgoing = fruits[left]
                basket[outgoing] -= 1
                if basket[outgoing] == 0:
                    del basket[outgoing]
                left += 1
            count = i - left + 1
            max_count = max(max_count, count)
        return max_count
