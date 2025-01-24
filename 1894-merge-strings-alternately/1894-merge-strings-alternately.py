class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        Sketch:

        W1 = [A B C D O P]

        W2 = [P B R C]

        OUTPUT - APBBCRDCOP


        ALgo:

        Two pointer 

        i - word 1 
        j - word 2 

        out of bound append extra word

        TC: o(n + m)

        SC: o(n + m )

        '''

        i = 0 
        j = 0 

        res = []

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[i])

            i += 1
            j += 1 

        res.append(word1[i:])
        res.append(word2[j:]) 

        return "".join(res)
        