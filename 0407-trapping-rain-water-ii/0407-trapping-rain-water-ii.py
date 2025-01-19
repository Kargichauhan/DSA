class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        #graph traversal
        if not heightMap:
            return 0 

        m,n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0 


        heap = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True


        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_water = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    if heightMap[nx][ny] < height:
                        total_water += height - heightMap[nx][ny]
                        heightMap[nx][ny] = height
                    visited[nx][ny] = True
                    heapq.heappush(heap, (heightMap[nx][ny], nx, ny))
        
        return total_water




        