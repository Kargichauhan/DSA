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
        write = 0 
        read = 0 

        while read < len(chars):
            char = chars[read]
            count = 0 

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1 
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write


        



        





        




        