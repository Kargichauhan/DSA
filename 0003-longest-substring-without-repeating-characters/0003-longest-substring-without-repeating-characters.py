class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            charS = set()
            for j in range(i, len(s)):
                if s[j] in charS:
                    break
                charS.add(s[j])
            res = max(res, len(charS))

        return res
        
