class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        #Time Complexity: O(m+n)
        #Space Complexity: O(n)
        r_dict = {}
        m_dict = {}

        for letter in ransomNote:
            try:
                r_dict[letter] += 1
            except:
                r_dict[letter] = 1

        for letter in magazine:
            try:
                m_dict[letter] += 1
            except:
                m_dict[letter] = 1

        for letter in r_dict.keys():
            if r_dict[letter] > m_dict.get(letter, 0):
                return False
        return True
            
