class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(" ")
        if not s:
            return 0
        res = ""
        r = False
        i = 0
        if s[i] in ["-","+"]:
            if s[i]=="-":
                r = True
            i+=1
        while i<len(s) and s[i].isdigit():
            res += s[i]
            i+=1
        if not res:
            return 0
        res = int(res)
        if r:
            res =-res
        minran = -2**31
        maxran = 2**31-1
        if res < minran:
            return minran
        if res > maxran:
            return maxran
        return res