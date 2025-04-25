class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window
             i      j 
        s = "abcabcbb"
        0 = 3
        '''

        i = 0 
        max_len = 0 
        seen = set()

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            seen.add(s[j])
            max_len = max(max_len,j - i + 1)

        return max_len


        



            

        
