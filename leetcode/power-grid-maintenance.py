class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)

        status = [1] * (c + 1)
        componentHeap = defaultdict(list)
        seen = set()

        def dfs(i, component):
            seen.add(i)
            component.append(i)
            
            for nei in graph[i]:
                if nei not in seen:
                    dfs(nei, component)

        for i in range(1, c+1):
            if i not in seen:
                component = []
                dfs(i, component)
                heapq.heapify(component)
                for n in component:
                    componentHeap[n] = component

        for task, node in queries:
            if task == 2:
                status[node] = 0
            else:
                if status[node] == 1: 
                    res.append(node)
                elif not componentHeap[node]:
                    res.append(-1)
                else:
                    while (status[componentHeap[node][0]] == 0):
                        heapq.heappop(componentHeap[node])
                        if not componentHeap[node]:
                            res.append(-1)
                            break
                    if componentHeap[node]:
                        res.append(componentHeap[node][0])


        return res