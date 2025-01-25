class Solution:
    def reverseWords(self, s: str) -> str:
        '''

        sketch:

         s = "the sky is blue"
            "blue is sky the"

            seperate word by whitespaces


        

        Algo:

        split to remove whitespace


        TC:

        SC:



        '''

        return " ".join(reversed(s.split()))

        
        