class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: float) -> bool:
            hoursUsed = 0
            for pile in piles:
                if k != 0:
                    hoursUsed += math.ceil(float(pile) / k)

            return hoursUsed <= h
        
        minK = -1

        l, r = 1, max(piles)

        while l <= r:
            # k = (l + r) // 2
            k = l + ((r - l) // 2) #try this one later
            if canFinish(k):
                minK = k
                r = k - 1
            else:
                l = k + 1
        
        return minK
