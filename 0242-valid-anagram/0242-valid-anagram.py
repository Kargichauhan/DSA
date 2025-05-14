class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        store in hashmap to check number of elements/words
        '''

        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

        

        

        