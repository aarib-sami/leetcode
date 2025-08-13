class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        graph = defaultdict(list)

        for ver, nei in edges:
            graph[ver].append(nei)
            graph[nei].append(ver)

        visit = set()

        def dfs(n):
            if n in visit:
                return 0

            visit.add(n)

            for nei in graph[n]:
                dfs(nei)

            return 1
            
        for i in range(n):
            res += dfs(i)

        return res