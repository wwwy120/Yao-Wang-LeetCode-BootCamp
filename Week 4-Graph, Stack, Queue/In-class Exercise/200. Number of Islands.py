class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        #Time Exceeded for large m and n
        m, n = len(grid), len(grid[0])

        lst = []
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    v = []
                    v += [r * n + c]
                    if c < n - 1 and grid[r][c + 1] == '1': #right
                        v += [r * n + (c + 1)]
                    if c > 0 and grid[r][c - 1] == '1': #left
                        v += [r * n + (c - 1)]
                    if r < m - 1 and grid [r + 1][c] == '1': #bottome
                        v += [(r + 1) * n + c]
                    if r > 0 and grid [r - 1][c] == '1': #top
                        v += [(r - 1) * n + c]
                    lst += [v]

        if len(lst) == 0:
            return 0
        elif len(lst) == 1:
            return 1

        print(lst)
        i = 0
        j = 0
        while True:
            if i == j:
                j += 1
            if j == len(lst):
                i += 1
                j = i + 1
            if i >= len(lst) - 1:
                break
            set1 = set(lst[i])
            set2 = set(lst[j])
            if set1 - set2 != set1:
                lst.append(list(set1.union(set2)))
                lst.pop(j)
                lst.pop(i)
                j = i + 1
            else:
                j += 1

        return len(lst)
