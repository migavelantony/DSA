# LeetCode 682: Baseball Game
# Source: https://leetcode.com/problems/baseball-game/description/
#
# Problem summary (paraphrased):
# Process a score log: an integer adds a score, + adds the sum of the previous two, D
# adds twice the previous score, and C removes the previous score. Return the remaining
# score total.

class Solution(object):

    def calPoints(self, operations):
        results = []
        for op in operations:
            if op == 'C':
                results.pop()
            elif op == 'D':
                results.append(2 * results[-1])
            elif op == '+':
                results.append(results[-1] + results[-2])
            else:
                results.append(int(op))
        return sum(results)
