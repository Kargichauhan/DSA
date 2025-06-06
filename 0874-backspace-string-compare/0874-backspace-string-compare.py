class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string: str) -> str:
            ans = []
            for c in string:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)

        return build(s) == build(t)

        



