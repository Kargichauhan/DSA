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
        return [c + extraCandies >= maxCandies for c in candies]



        



        


        