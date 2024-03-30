class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == '':
            return True
        else:
            if s[0] == '(':
                obj = ')'
            elif s[0] == '[':
                obj = ']'
            else:
                obj = '}'
            
            inside = ""
            remain = ""
            count_left = 1
            count_right = 0
            for i in range(1, len(s)):
                if count_left < count_right:
                    return False
                if s[i] == s[0]:
                    count_left += 1
                elif s[i] == obj:
                    count_right += 1
                    if count_left == count_right:
                        inside = s[1:i]
                        remain = s[i+1:]
                        break
            if count_left != count_right:
                return False
            return self.isValid(inside) and self.isValid(remain)
                
        
