class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        res = 1

        while n:
            if n % 2 == 1:
                res *= x
            n >>= 1
            x *= x
        return res