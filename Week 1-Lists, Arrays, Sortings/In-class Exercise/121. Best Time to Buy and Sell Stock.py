class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                if p - min_price > max_profit:
                    max_profit = p - min_price
        return max_profit
