class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        N = limit + 1
        f = collections.Counter()
        color = collections.defaultdict(lambda: 0)

        

        ans = []
        for x,y in queries:
            prev = color[x]
            if prev != 0:
                f[prev] -= 1
                if f[prev] == 0:
                    del f[prev]

            color[x] = y
            f[y] += 1
            ans.append(len(f))

        return ans

        