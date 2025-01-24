class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Sketch:

        W1 = [A B C D O P]

        W2 = [P B R C]

        OUTPUT - APBBCRDCOP


        ALgo:

        Two pointer + string traversal

        i - word 1 
        j - word 2 

        out of bound append extra word

        TC: o(n + m)

        SC: o(n + m )

        '''

        

        res = []

        min_len = min(len(word1), len(word2))

        '''for i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[i])'''

        for i in range(min_len):
            res.append(word1[i])
            res.append(word2[i])

        if len(word1) > len(word2):
            res.append(word1[min_len:])
        else:
            res.append(word2[min_len:])

        return "".join(res)
        