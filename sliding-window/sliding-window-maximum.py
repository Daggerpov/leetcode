"""
Go through nums with right pointer, as usual. For each char seen, keep popping from the queue
if it's greater than that right-most element of queue. Then, append it onto the queue → which
will store indexes, like this r.

If l is greater than the index of the first element in the queue, then pop the left element of
queue, since it's no longer valid as the max in that sliding window, since it should be outside
of that window.

if (r + 1) >= k: append to res, since it's the maximum at this window. Also, increment l,
since we can know that the current window is of size k.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque()  # index
        l = 0

        for r in range(len(nums)):
            # prune away elements that can't be the maximum
            # since they were added before the current
            # num and are < the current num, `nums[r]`
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # to compensate for the r increase,
            # need to get rid of the oldest added element
            if l > q[0]:
                q.popleft()

            # ensuring we've gotten to the kth index,
            # since prior iterations wouldn't have been
            # of window size k
            if (r + 1) >= k:
                # start to append the maximal element
                # inside of the current window
                output.append(nums[q[0]])
                l += 1

        return output
