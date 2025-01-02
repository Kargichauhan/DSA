class Solution:
    def decodeString(self, s: str) -> str:
        def ans(self, s):
            if s.count('[') == 0:
                return s 
            for x in range(len(s)):
                if s[x] == '[':
                    i = x - 1
                    k = ""
                    self.c = 0
                    while i >-1 and s[i].isdigit():
                        k += s[i]
                        i -= 1
                        self.c += 1
                    k = k[::-1]
                    k = int(k)

                    mx = x - self.c
                if s[x] == ']':
                    my = x - 1
                    t = ""
                    t += k * s[mx + self.c + 1: my + 1]
                    s = s[:mx] + t + s[my + 2:]
                    return ans(self, s)
        return ans(self,s)
