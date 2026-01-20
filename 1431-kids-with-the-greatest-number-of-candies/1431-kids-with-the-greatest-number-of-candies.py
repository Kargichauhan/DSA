class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        # greatest num of candies 

        # for each kid - check if they will have greates no. of candies 
        # among all the kids

        res = []
        for i in range(len(candies)):
            res.append(candies[i] + extraCandies >= maxCandies)

        return res



        #tc: 0(n)
        #sc: 0(1)





        