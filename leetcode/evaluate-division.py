class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i, val in enumerate(equations):
            n1, n2 = val
            graph[n1].append([n2, values[i]])
            graph[n2].append([n1, 1 / values[i]])

        def bfs(src, tar):
            queue = deque()
            queue.append([src, 1])
            visit = set()

            if src not in graph.keys() or tar not in graph.keys():
                return -1

            while queue:
                n, val = queue.popleft()
                visit.add(n)
                if n == tar:
                    return val

                for neighbour, wei in graph[n]:
                    if neighbour not in visit:
                        queue.append([neighbour, val * wei])

            return -1

        return [ bfs(src, tar) for src, tar in queries ]