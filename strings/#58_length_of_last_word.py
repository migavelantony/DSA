# LeetCode 58: Length of Last Word
# Source: https://leetcode.com/problems/length-of-last-word/description/
#
# Problem summary (paraphrased):
# Count the characters in the final word of a string, ignoring any spaces at the end.
# Words are separated by spaces.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])


sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
