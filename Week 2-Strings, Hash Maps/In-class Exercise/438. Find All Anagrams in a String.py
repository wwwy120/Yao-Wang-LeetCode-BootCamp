class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        #Time Complexity: O(N)
        #Space Complexity:O(N)
        if len(p) > len(s):
            return []
        
        dic_p, dic_s = {}, {}

        for letter in p:
            dic_p[letter] = dic_p.get(letter, 0) + 1

        for i in range(len(p)):
            dic_s[s[i]] = dic_s.get(s[i], 0) + 1
        
        res = []
        for i in range(len(s) - len(p) + 1):
            if dic_p == dic_s:
                res += [i]
            if i != len(s) - len(p):
                dic_s[s[i]] = dic_s.get(s[i], 0) - 1
                if dic_s[s[i]] == 0:
                    del dic_s[s[i]]
                dic_s[s[i+len(p)]] = dic_s.get(s[i+len(p)], 0) + 1

        return res

        



