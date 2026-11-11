# LeetCode 43: Multiply Strings
# Source: https://leetcode.com/problems/multiply-strings/description/
#
# Problem summary (paraphrased):
# Multiply two nonnegative integers supplied as digit strings and return their product
# as a string. Do not parse either complete input as an integer or use a big-integer
# library.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return 0

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                prod = (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0"))
                total = prod + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        k = 0
        while k < len(result) - 1 and result[k] == 0:
            k += 1

        return "".join(map(str, result[k:]))


sol = Solution()
print(sol.multiply("5", "2"))
print(sol.multiply("123", "456"))
