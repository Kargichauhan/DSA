class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) # map {a: [[b, 2], [c, 1]]}
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(start, target):
            if start not in adj or target not in adj:
                return -1
            queue = deque()
            visit = set()
            queue.append([start, 1])
            visit.add(start)
            while queue:
                n, w = queue.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        queue.append([nei, w*weight])
                        visit.add(nei)
            return -1

        return [bfs(q[0], q[1]) for q in queries]