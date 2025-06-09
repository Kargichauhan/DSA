from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        @lru_cache(None)
        def dp(i, days_left):
            if days_left == 1:
                return max(jobDifficulty[i:])
            
            res = float('inf')
            cur_max = 0

            # j is the last job index for current day
            for j in range(i, n - days_left + 1):
                cur_max = max(cur_max, jobDifficulty[j])
                res = min(res, cur_max + dp(j + 1, days_left - 1))
            
            return res

        return dp(0, d)
