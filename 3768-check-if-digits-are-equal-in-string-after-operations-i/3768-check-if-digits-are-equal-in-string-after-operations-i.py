class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ""

            for i in range(len(s)-1):
                dig1 = int(s[i])
                dig2 = int(s[i+1])

                new_d = (dig1+dig2) % 10

                new_s += str(new_d)

            s = new_s
            #print(f"After iteration: s = {s}, len = {len(s)}") 

        return s[0] == s[1]