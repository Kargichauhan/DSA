class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        bitwise XOR 

        
        '''

        isOdd = 0 
        for c in s:
            isOdd ^= 1 << (ord(c) -ord('a'))
        return isOdd & (isOdd -1) == 0
        