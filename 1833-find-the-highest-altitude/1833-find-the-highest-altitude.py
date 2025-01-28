class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        '''
        Sketch:

        N + 1 -> points 
        starts -> 0 
        al = 0

        len n 

        Input: gain = [-5,1,5,0,-7] range of the altitude 

        = [0, -5, -4, 1, 1, ].     
        
        -5 + 1  = - 4 , -4 + 5 = 1, 1+ 0 = 1, 1 + -6 = 7 
        [0, -5, -4, 1, 1-7 ] = 1 (highest)
        Output: 1

        Algo:
        TC:
        SC:
        '''

        alt = 0

        max_alt = 0 


        for change in gain:
            alt += change
            max_alt = max(max_alt, alt)

        return max_alt

        