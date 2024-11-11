class Solution(object):
    def romanToInt(self, s):
        
        """
        :type s: str
        :rtype: int
        """
        roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
        res = 0
        prev= 0
        for char in reversed(s):
            cur = roman_values[char]
            if cur < prev:
                res -= cur
            else:
                res += cur
            prev = cur
    
        return res


        pass



