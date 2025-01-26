class Solution:
    def compress(self, chars: List[str]) -> int:
        
        '''
        SKETCH: 

        chars
        Input: chars = ["a","a","b","b","c","c","c"]

        



        ALGO:

        [a, a , b, c , c , c]
        0.  1.  2  3.  4.  5

        pointer 

        currchar = 

        curr occ

        TC: o(n)

        SC:

        
        '''

        r , i = 0 , 0

        while (i < len(chars)):
            currChar = chars[i]

            currOcc = 0


            while ((i < len(chars)) and (chars[i] == currChar)):
                currOcc += 1
                i += 1

            

            chars[r] = currChar

            r += 1

            if (currOcc > 1):
                currOccStr = str(currOcc)
                for j in range(len(currOccStr)):
                    chars[r] = currOccStr[j]
                    r += 1
        return r




        





        




        