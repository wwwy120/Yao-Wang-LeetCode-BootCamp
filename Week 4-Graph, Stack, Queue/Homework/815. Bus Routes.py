class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """

        if source == target:
            return 0
        
        v = set()
        for lst in routes:
            v = v.union(set(lst))
        v = list(v)

        if max(v) < target:
            return -1

        lst = [0] * (max(v)+1)

        graph = {}
        for vertice in v:
            graph[vertice] = []
            edge = []
            for route in routes:
                subedge = []
                for stop in route:
                    if stop != vertice:
                        subedge += [stop]
                if len(subedge) != len(route):
                    edge += subedge
            graph[vertice] = edge
        
        
        bus(graph, lst, source, target)
        if lst[target] == 0:
            return -1
        return lst[target]
        
