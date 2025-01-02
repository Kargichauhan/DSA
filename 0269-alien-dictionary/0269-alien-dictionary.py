class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nei = defaultdict(set)
        indegree = defaultdict(set)
        chars = set()

        n = len(words)

        for i in range(n):
            chars = chars | set(words[i])
            for j in range(i):
                curr = words[i]
                prev = words[j]

                l, r = 0, 0
                while l < len(curr) and r < len(prev) and curr[l] == prev[r]:
                    l += 1 
                    r += 1


                if l < len(curr) and r < len(prev):
                    char = prev[r]
                    char_after = curr[l]


                    if char in nei[char_after]:
                        return ""

               

                    nei[char].add(char_after)
                    indegree[char_after].add(char)
                elif r < len(prev):
                    return ""



        queue = deque()
        for c in chars:
            if c not in indegree:
                queue.append(c)


        ans = []
        while queue:
            c = queue.popleft()
            ans.append(c)

            for n in nei[c]:
                indegree[n].discard(c)
                if len(indegree[n]) == 0:
                    queue.append(n)


        return "".join(ans)


                   

                



        