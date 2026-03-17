class Solution(object):
    def isPalindrome(self, x):
        original = x #124
        palindrome = 0

        while x > 0:
            last_digit = x % 10 #4
            palindrome = palindrome * 10 + last_digit #4 = 0 * 10 + 4
            x = x // 10 # 12 = 124 // 10
        
        return palindrome == original 


        