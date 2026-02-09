"""
Loop through nums, calling heapq.heappush(numsMaxHeap, -n), pushing the negative of each value. Then, loop for in in range(len(nums)):, calling elem = -1 * heapq.heappop(numsMaxHeap) to get the original number. return the number once k has been decremented down to 0
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Select solution: O(n) average, O(n^2) worst case time complexity

        # Heap Solution:
        '''
        numsMaxHeap = []
        count = 0
        
        for n in nums:
            heapq.heappush(numsMaxHeap, -1 * n)
            '''
        numsMaxHeap = [-n for n in nums]
        heapq.heapify(numsMaxHeap)

        count = 0
        
        for i in range(len(nums)):
            elem = -1 * heapq.heappop(numsMaxHeap)
            count += 1
            if k == count:
                return elem

        return 

# Alternative solution:
# Quick Select

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)
