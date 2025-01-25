class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ''''

        Sketch:

        Candies = [2,3,5,1,3] 
        extraCandies = 3

        [5,6,8,4,6]
        [true,true,true,false,true] 


        Algo: max num - iterate thru list of max no. of candies any child currently has 

        TC: constant

        SC: constant
        
        
        '''


        maxi = max(candies)
        res = []

        for candy in candies:
            if candy + extraCandies >= maxi:
                res.append(True)

            else: res.append(False)


        return res




        