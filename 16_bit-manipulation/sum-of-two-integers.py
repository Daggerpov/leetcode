class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry_bit = 0
        res = 0
        mask_32_bit = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a>>i) & 1
            b_bit = (b>>i) & 1

            # summation
            current_bit = a_bit ^ b_bit ^ carry_bit
            carry_bit = 1 if (a_bit + b_bit + carry_bit) >= 2 else 0

            if current_bit == 1:
                res |= (1 << i)

        # If first bit is set to 1, it's negative 
        # So, take 32-bit two's complement
        mask_31_bit = 0x7FFFFFFF
        if res > mask_31_bit:
            res = ~(res ^ mask_32_bit)

        return res
