class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) +1, len(edges2) + 1
        A = [[] for _ in range(n)]
        B = [[] for _ in range(m)]

        for u, v in edges1:
            A[u].append(v)
            A[v].append(u)

        for u, v in edges2:
            B[u].append(v)
            B[v].append(u)


        def ball(G,R):
            cnt = []
            for i in range(len(G)):
                d = [-1] * len(G)
                d[i] = 0;q = deque([i])
                while q:
                    u = q.popleft()
                    if d[u] == R: continue

                    for v in G[u]:
                        if d[v] < 0:
                            d[v] = d[u] + 1
                            q.append(v)

                cnt.append(sum(dj >= 0 for dj in d))

            return cnt

        c1 = ball(A, k)
        c2 = ball(B, k - 1) if k > 0 else [0] * m
        bonus = max(c2) if c2 else 0
        return [x + bonus for x in c1]

