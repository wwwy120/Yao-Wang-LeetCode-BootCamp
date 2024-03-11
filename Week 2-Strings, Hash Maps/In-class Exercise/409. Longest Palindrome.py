class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        d = {}
        for letter in s:
            try:
                d[letter] += 1
            except:
                d[letter] = 1
        
        odd = False
        res = 0
        for value in d.values():
            if value % 2 == 0:
                res += value
            else:
                odd = True
                res += (value - 1)
        if odd:
            res += 1
        return res
