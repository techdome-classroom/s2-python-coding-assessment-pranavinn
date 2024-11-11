class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching_brackets:
                if not st or st.pop() != brackets[char]:
                    return False
            else:
                st.append(char)
        return not st

        pass







    



  

