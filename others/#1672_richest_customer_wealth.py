# LeetCode 1672: Richest Customer Wealth
# Source: https://leetcode.com/problems/richest-customer-wealth/description/
#
# Problem summary (paraphrased):
# Each matrix row lists one customer's bank balances. Return the largest row sum,
# representing the greatest total customer wealth.

class Solution(object):

    def maximumWealth(self, accounts):
        richest = 0
        for account in accounts:
            acc_sum = 0
            for moeny in account:
                acc_sum = acc_sum + moeny
            if acc_sum > richest:
                richest = acc_sum
        return richest
