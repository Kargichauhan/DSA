
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        s = collections.defaultdict(list)

        for x in nums:
            s[sum(int(c) for c in str(x))].append(x)

        best = -1
        for y in s.keys():
            if len(s[y]) >= 2:
                s[y].sort()
                s[y].reverse()

                best = max(best,s[y][0] + s[y][1])

        return best 

        
        