class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0

        # We only care about windows of size 3
        for i in range(len(s) - 2):
            window = s[i:i+3]
            # If all 3 characters are unique, count it
            if len(set(window)) == 3:
                res += 1

        return res