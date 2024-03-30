class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        import collections

        deck.sort()
        res = collections.deque()
        while deck != []:
            res.append(deck.pop())
            if deck != []:
                res.append(res.popleft())
        res.reverse()
        return res
