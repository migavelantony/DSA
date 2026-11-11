# LeetCode 151: Reverse Words in a String
# Source: https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# Problem summary (paraphrased):
# Return the words of the input string in reverse order. Use one space between words
# and remove leading and trailing spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.split()
        left = 0
        right = len(word) - 1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        # return " ".join(word[::-1])
        return " ".join(word)


sol = Solution()
print(sol.reverseWords(" the sky is blue "))
