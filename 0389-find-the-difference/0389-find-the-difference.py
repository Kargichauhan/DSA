class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        bit manipulation
        bitwise -> XOR -> help eliminate the alike and only leve the odd duckling
        '''

        #initializing ch with 0, bcz 0 ^ x = x so when XOred with any bit would 
        # not change the bits value


        ch = 0

        #xor all the char of both s and t

        for char_ in s:
            ch ^= ord(char_)

        for char_ in t:
            ch ^= ord(char_)



        #what is left after xoring everything is difference
        return chr(ch)


        
        













































        