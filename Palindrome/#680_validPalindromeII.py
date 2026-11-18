# LeetCode 680: Valid Palindrome II
# Source: https://leetcode.com/problems/valid-palindrome-ii/description/
#
# Problem summary (paraphrased):
# Determine whether a string can become a palindrome after deleting at most one
# character.

class Solution(object):

    def validPalindrome(self, s):
        left, right = (0, len(s) - 1)
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
