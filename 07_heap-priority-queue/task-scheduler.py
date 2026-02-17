# TODO: explain

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = Counter(tasks)
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = (-1 * heapq.heappop(maxHeap)) - 1
                if cnt != 0:
                    q.append([-1 * cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
