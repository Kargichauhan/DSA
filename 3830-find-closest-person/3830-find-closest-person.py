class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # bcz all of them are matched based on speed and speed is 
        # identical deciding factor will be distance 

        # d(first-third person) = |x-z|
        # d(second-third person) = |y-z|

        dxz = abs(x-z)
        dyz = abs(y-z)

        if dxz < dyz:
            return 1
        elif dxz > dyz:
            return 2

        else:
            return 0 

