class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        dels = 0 

        for c in range(cols):
            for r in range(rows-1):
                if strs[r][c] > strs[r+1][c]:
                    dels += 1
                    break
        return dels