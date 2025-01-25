class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)


        def isDivisor(l):
            if len1 % l != 0 or len2 % l != 0:
                return False


            

            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2


        for l in range(min(len1, len2), 0 , -1):
            if isDivisor(l):
                return str1[:l]

        return ""


        '''        Sketch:

        Input:   str1 = "ABCABC"
                 str2 = "ABC"

        Output: "ABC"

        Input: str1 = "LEET"
            str2 = "CODE"
        Output: ""

        ALgo:

        Brute force:

        substring ABABAB

        ABAB [A] 

        L1 % Length = 0 



        

        TC: o(n + m) . (m.n)

        SC: o(n + m) . (m.n)



        '''



        




