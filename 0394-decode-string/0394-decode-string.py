class Solution:
    def decodeString(self, s: str) -> str:
        encode_s = []
        num = 0 
        temp = ""

        for i in s:
            if i.isdigit():
                num = (num * 10) + int(i)


            elif i == '[':
                encode_s.append((temp, num))
                num = 0 
                temp = ""


            elif i == ']':
                string,nums = encode_s.pop()
                temp = string + (temp * nums)

            else:
                temp += i

        return temp
                

        


        