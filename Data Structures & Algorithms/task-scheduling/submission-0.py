class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #get most freq elements
        count = Counter(tasks)
        #make max heap using counts
        maxheap = [-counts for counts in count.values()]#have to negate the vals
        heapq.heapify(maxheap)#to get max vals
        time = 0
        queue = deque()#will store the (-count,idleTime)
        
        while maxheap or queue:
            time += 1
            if maxheap:
                count = 1 + heapq.heappop(maxheap)#pop from heap -> processing the task, add one to reduce freq
                if count != 0: 
                    queue.append([count,time + n])
            if queue and queue[0][1] == time:#if idle time has been reach pop from queue to signify that we can reprocess the task if needed
                heapq.heappush(maxheap, queue.popleft()[0])
        return time
