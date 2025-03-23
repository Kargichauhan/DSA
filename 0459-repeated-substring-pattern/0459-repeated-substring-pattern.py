class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        '''
        using divisors

        string concatenation
        '''

        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                pattern = s[:i] * (n // i)
                if s == pattern:
                    return True
        return False
        

        