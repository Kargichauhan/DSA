class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        for i in range(len(s) -1, -1, -1):
            for j in range(0, len(s) - i + 1):

                if s[j : i + j] in s[j + 1:]: return i 

        return 0 

        