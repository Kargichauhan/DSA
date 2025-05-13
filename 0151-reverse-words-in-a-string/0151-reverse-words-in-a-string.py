class Solution:
    def reverseWords(self, s: str) -> str:
        '''

        sketch:

         s = "the sky is blue"
            "blue is sky the"

            seperate word by whitespaces

        Algo:

        split to remove whitespace


        TC: o(n)

        SC: o(n)



        '''

        return " ".join(reversed(s.split()))

        

        
        