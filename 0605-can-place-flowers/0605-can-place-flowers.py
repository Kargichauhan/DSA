class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        breakdown:
        -> flowerbed (plants)
        -> cannot be planted in adjacent plots

        0's = empty
        1's = non-empty

        Approach:
        flowerbed in array 
        greedy 


        empty flowerbed 


        '''

        for i in range(len(flowerbed)):
            # only try to plant in an empty spot
            if flowerbed[i] == 0:
                empty_left  = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1  # plant here
                    n -= 1
                    if n == 0:
                        return True
        return n <= 0



        

         



        


        