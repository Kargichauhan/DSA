class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        breakdown:

        -> merge the string by adding letters
        -> letters in the alternating order 
        -> if the len of word is > other other then add 
        that greater word len to the end of merged string

        Approach:

        -> two pointer
        -> sliding window 

        word 1 (i) -> pointer will go over each index of word 1
        word 2 (j) -> pointer will go over each index of word 2

        res = [] -> output alternative combination

        edge case: lower case (case sensitive) + no words ?

        Complexity

        o(n + m) -> time complexity
        o(1) -> SC

        '''

        i, j = 0, 0 
        res = []

        while i  < len(word1) and j < len(word2): # INBOUND 
            res.append(word1[i]) # OUTPUT -> APPEND
            res.append(word2[j])

            i += 1 # increment 
            j += 1

        res.append(word1[i:]) # IF WORDS NOT SAME LEN -> COMBINE THE REMANING
        res.append(word2[j:])

        return "".join(res) #JOIN THE RES


        

        

