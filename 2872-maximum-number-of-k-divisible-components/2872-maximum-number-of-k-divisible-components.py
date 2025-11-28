class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        components = 0 

        def dfs(node, parent):
            nonlocal components
            total = values[node]
            for child in graph[node]:
                if child != parent:
                    total += dfs(child, node)
            if total % k == 0:
                components += 1
            return total

        total_sum = dfs(0, -1)
        return components if total_sum % k == 0 else 0 



        