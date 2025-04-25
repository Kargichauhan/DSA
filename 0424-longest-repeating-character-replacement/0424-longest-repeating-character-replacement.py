class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0 
        res = 0 
        i = 0 

        for j in range(len(s)):
            count[s[j]] += 1
            max_count = max(max_count, count[s[j]])

            while (j - i + 1) - max_count > k:
                count[s[i]] -= 1

                i += 1 
            res = max(res, j - i + 1)

        return res
