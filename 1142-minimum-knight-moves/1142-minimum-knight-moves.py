class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)

        steps = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        q = deque([(0,0,0)])
        seen = set((0,0))

        while q:
            i, j, moves = q.popleft()
            if (i, j) == (x,y):
                return moves

            for dx, dy in steps:
                ni, nj = i + dx, j + dy

                if (ni, nj) not in seen and -2 <= ni <= x + 2 and -2 <= nj <= y + 2:
                    seen.add((ni, nj))
                    q.append((ni, nj, moves + 1))
        