class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        word 1 and word 2 - merge string 


        two index i -> word 1 
        j -> word 2 

        1. create len of m and n to store len of word 1 n word 2 
        2. res -> variable 
        3. two pointers i and j -> to point indices of word 1 and word 2 
        4. while loop 




        '''

        m = len(word1)
        n = len(word2)

        i = 0 
        j = 0 

        res = []


        while i < m or j < n:
            if i < m:
                res += word1[i]
                i += 1

            if j < n:
                res += word2[j]
                j += 1


        return "".join(res)
        