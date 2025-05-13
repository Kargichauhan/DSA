class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set('aeiouAEIOU')

        res = []

        for ch in s:
            if ch in vowels:
                res.append(ch)

        res.reverse()

        out_chars = []
        vi = 0 #index into extracted list

        for ch in s:
            if ch in vowels:
                out_chars.append(res[vi])
                vi += 1

            else: out_chars.append(ch)


        return "".join(out_chars)



        