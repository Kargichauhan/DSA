from collections import Counter 

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Sketch:

        operation 1 -> abcde - aecdb
        operation 2 -> aacabb - bbcbaa



        Algo:

        Input: word1 = "abc", word2 = "bca"
        Output: true

        #1 length
        #2 char 
        # 3. frequency



        TC:

        SC:


        '''

        if len(word1) != len(word2):
            return False

        counts1 = Counter(word1)
        counts2 = Counter(word2)

        return (counts1.keys() == counts2.keys()) and (sorted(counts1.values()) == sorted(counts2.values()))

        






        




        


            


        