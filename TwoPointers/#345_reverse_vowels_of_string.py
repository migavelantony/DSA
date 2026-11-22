# LeetCode 345: Reverse Vowels of a String
# Source: https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# Problem summary (paraphrased):
# Reverse only the vowels in the string while leaving all other character positions
# unchanged. Both uppercase and lowercase vowels count.

class Solution(object):

    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        left = 0
        right = len(s) - 1
        word = list(s)
        while left < right:
            if word[left] in vowels and (not word[right] in vowels):
                right -= 1
            elif word[right] in vowels and (not word[left] in vowels):
                left += 1
            elif word[left] in vowels and word[right] in vowels:
                word[left], word[right] = (word[right], word[left])
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1
        return ''.join(word)
