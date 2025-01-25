class Solution:
    def reverseVowels(self, s: str) -> str:
        '''
        Sketch:

        A D I O S 

        |   |  |
        O D  I   A S


    

        Algo:

        Two - pointer 

        TC:

        SC:


        '''
# string as mutuable so convert to list
        s = list(s)

        vowels = set('aeiouAEIOU')

        i, j = 0, len(s) - 1


        while i < j: 
            if (s[i] not in vowels):
                i += 1

            elif s[j] not in vowels:
                j -= 1

            else: 
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''. join(s)



        