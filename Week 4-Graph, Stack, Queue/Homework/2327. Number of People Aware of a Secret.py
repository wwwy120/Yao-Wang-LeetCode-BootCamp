class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """

        #Time Complexity: O(n * (forget - delay))
        #Space Complexity: O(n)
        d = [0] * (n+1)
        d[1] = 1
        for i in range(1, n + 1):
            if d[i] > 0:
                dl = i + delay
                fg = i + forget
                day_share = min(fg, n+1)
                for j in range(dl, day_share):
                    d[j] += d[i]
                
                if fg <= n:
                    d[i] = 0
        
        return sum(d) % (10**9 + 7)



        # Time Exceeded for large data
        import collections
        queue = collections.deque()
        queue.append(1)
        for i in range(2, n + 1):
            pop = 0
            for j in range(len(queue)):
                if i - queue[j] == forget:
                    pop += 1
                elif i - queue[j] >= delay:
                    queue.append(i)
            for i in range(pop):
                queue.popleft()
        
        return len(queue) % (10 ** 9 + 7)


                

        
