class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            graph[v].append(u)
            graph[u].append(v)

        indegree = [len(neighbors) for neighbors in graph]
        queue = deque(node for node in range(len(edges)+1) if indegree[node] == 1)
        while queue:
            next_node = queue.popleft()
            for neighbor in graph[next_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 1:
                    queue.append(neighbor)

        for u, v in reversed(edges):
            if indegree[u] == 2 and indegree[v] == 2:
                return [u, v]
        