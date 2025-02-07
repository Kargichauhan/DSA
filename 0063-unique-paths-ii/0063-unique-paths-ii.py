class Solution(object):
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        dp = [0] * N 
        dp[N-1] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0

                elif c + 1 < N:

                    dp[c] = dp[c] + dp[c+1]

        return dp[0]


        




         

    


      