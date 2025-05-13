class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        breakdown:
        -> s and t string 
        -> str1 * str2 = str1 + str2

        approach:
        -> string 
        -> pointer over str1 and str2 
        -> most common = output



        Complexity:
        o(n) = tc
        o(n) = sc

        '''
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % 1 != 0 or len2 % 1 != 0:
                return False

            f1, f2 = len1 // l , len2 // l

            base = str1[:l]

            return base * f1 == str1 and base * f2 == str2


        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""


        

            

        

        


        