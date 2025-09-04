class Solution:
    def reverseVowels(self, s: str) -> str:
        V = "aeiouAEIOU"
        rv = iter([c for c in s if c in V][::-1])
        return "".join(next(rv) if c in V else c for c in s)

