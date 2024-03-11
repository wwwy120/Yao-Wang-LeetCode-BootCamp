class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        #Time Complexity: O(n)
        #Space Complexity: O(n)
        res = 0
        d = {}
        left = 0
        for right in range(len(s)):
            if s[right] not in d:
                d[s[right]] = 1
            else:
                d[s[right]] += 1
            
            if right - left + 1 - max(d.values()) > k:
                d[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left + 1))
        return res
