class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''
        Sketch:

        0 = empty 
        1 = not empty

        return True -> if new flower can be planted 

        Input: 
        
        flowerbed = [1,0,0,0,1]
        
        n = 1


        Output: true

        Algo:

        empty = 0 
        not_empty = 1 


        i -> iterate over the array 
        i -> 1 (count) -> true 
        adjacent


        TC: constant(1)


        SC: constant(1)


        '''

        if n == 0: return True


        for i in range(len(flowerbed)):
            left = (i == 0) or (flowerbed[i-1] == 0)
            right = (i == len(flowerbed) - 1) or flowerbed[i + 1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

                if n == 0: return True

        return False

         



        


        