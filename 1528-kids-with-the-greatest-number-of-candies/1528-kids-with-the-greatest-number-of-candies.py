class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        ''''
        Breakdown:

        -> kids = candies each [i] = number of candies ith kid have
        -> extracandies = extra candies you have

        -> true if after giving extra candies (greatest)
        -> false


        Approach:

        len(candies ) + extracandies = [res] 
        in the res -> greatest among or also use max[res] 
        min[res] = False other all true

        Complexity:

        o(n)
        o(n)

        '''

        maxCandies = max(candies)
        res = []


        for i in candies:
            if i + extraCandies >= maxCandies:
                res.append(True)

            else: res.append(False)

        return res



        



        


        