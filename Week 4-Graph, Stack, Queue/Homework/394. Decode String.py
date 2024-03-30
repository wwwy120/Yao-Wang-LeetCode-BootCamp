class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = 0
        string = ""
        res = ""
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == '[':
                stack.append(string)
                stack.append(num)
                string = ""
                num = 0
            elif char == ']':
                if not str(stack[-1]).isalpha():
                    stack.append(string)
                else:
                    stack[-1] += string
                string = ""
                while str(stack[-2]).isalpha() and str(stack[-1]).isalpha():
                    last = stack.pop()
                    stack.append(stack.pop() + last)
                stack.append(stack.pop() * stack.pop())
                last = stack.pop()
                stack.append(stack.pop() + last)
            else:
                string += char
        stack.append(string)
        return "".join(stack)
