class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        i = 0
        total = 0
        for i in range(len(s)):
            current = roman_numerals[s[i]]
            if i < len(s) - 1:
                next = roman_numerals[s[i+1]]
                if current < next:
                    total -= current
                else:
                    total += current
            else:
                total += current
        return total
        
        