class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        sign_done = False
        is_positive = True
        white_done = False
        res = 0
        for letter in s:
            if not white_done:
                if letter != ' ':
                    white_done = True
            if white_done:
                if not sign_done:
                    sign_done = True
                    if letter == '-':
                        is_positive = False
                        continue
                    elif letter == '+':
                        continue
                if sign_done:
                    try:
                        n = int(letter)
                        res *= 10
                        res += n
                    except:
                        break

        if not is_positive:
            res = -res
        if res > 2**31 - 1:
            return 2**31 - 1
        elif res < -2**31:
            return -2**31
        return res

        
