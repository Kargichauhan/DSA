class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in reversed(range(len(digits))):
            carry,digits[i] = divmod(digits[i] + carry, 10)


        if carry > 0:
            return[carry] + digits
        else: return digits




        

        