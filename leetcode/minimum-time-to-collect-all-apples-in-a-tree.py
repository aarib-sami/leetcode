class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        res = 0
        graph = defaultdict(list)
        seen = set()

        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)


        def dfs(i):
            res = 0

            seen.add(i)

            for tree in graph[i]:
                if tree in seen: continue
                
                val = dfs(tree)
                if val > 0 or hasApple[tree]: 
                    val += 2
                res += val

            return res

        return dfs(0)