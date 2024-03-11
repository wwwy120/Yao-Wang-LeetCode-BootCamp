class Solution(object):
    def isPalindrome(self, word):
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {}
        res = []
        for i in range(len(words)):
            d[words[i]] = i
        
        for word in words:

            reversed_word = word[:: -1]

            #Case 1: "" and palindrome is palindrome itself
            if self.isPalindrome(word) and word != "":
                if d.get("", None) != None:
                    res += [[d[word], d[""]]]
                    res += [[d[""], d[word]]]
            
            #Case 2: word and its reversed form
            elif (d.get(reversed_word, None) != None) and (d.get(reversed_word, None) != d[word]):
                res += [[d[word], d[reversed_word]]]
            
            #Case 3: 
            for i in range(1, len(word)):
                for fix in range(2):
                    if fix: #suffix
                        new_word = reversed_word[i:]
                        rest_word = reversed_word[:i]
                    else: #prefix
                        new_word = reversed_word[:i]
                        rest_word = reversed_word[i:]
                    
                    if self.isPalindrome(rest_word) and (d.get(new_word, None) != None):
                        if fix:
                            res += [[d[word], d[new_word]]]
                        else:
                            res += [[d[new_word], d[word]]]
            
        return res
                        


            
    
        
        


        
