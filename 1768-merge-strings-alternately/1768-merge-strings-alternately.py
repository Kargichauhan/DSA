class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)

        i = 0 
        j = 0 

        res = []

        while i < m or j < n:
            if i < m:  # not traversed word1
                res += word1[i] # append
                i += 1
            if j < n: # same not traversed 
                res += word2[j] # append
                j += 1

        return "".join(res)


        # TC: o(m+n)
        # SC: o(1) 