class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32): # [0, 31]
            bit = (n >> i) & 1
            res += bit << (32 - 1 - i)
        
        return res
