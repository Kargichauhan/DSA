class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])

        matrix = [[-1] * n for _ in range(m)] #same dimension as input

        que = deque()

        #initialize matrix and queue

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    que.append((i, j , 0))
                    matrix [i][j] = 0 


        directions = [(0,1), (0, -1),(1,0), (-1,0)]


        while que:
            r, c, height = que.popleft()
            for dr, dc in directions:
                nr,nc = r + dr, c + dc


                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] == -1:
                    matrix[nr][nc] = height + 1

                    que.append((nr, nc, height + 1))


        return matrix