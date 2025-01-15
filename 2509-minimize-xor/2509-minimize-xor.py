class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_set_bits(n):
            count = 0 
            while n:
                count += n & 1
                n >>= 1 
            return count 

        num2_set_bits = count_set_bits(num2)
        num1_set_bits = count_set_bits(num1)

        if num1_set_bits == num2_set_bits:
            return num1

        x = num1
        if num1_set_bits < num2_set_bits:
            diff = num2_set_bits - num1_set_bits
            i = 0 
            while diff > 0:
                if not (x & (1 << i)):
                    x |= (1 << i)
                    diff -= 1

                i += 1
        else:
            diff = num1_set_bits - num2_set_bits
            i = 0 
            while diff > 0:
                if x & (1 << i):
                    x ^= (1 << i)
                    diff -= 1
                i += 1
        return x

        