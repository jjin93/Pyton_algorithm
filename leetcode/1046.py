class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxHeap = list()
        for n in stones:
            heapq.heappush(maxHeap, -n)
            
        while len(maxHeap) > 1 :
            y = -heapq.heappop(maxHeap)
            x = -heapq.heappop(maxHeap)
            
            if x == y :
                continue
            else :
                heapq.heappush(maxHeap, -(y - x))
        
        return -heapq.heappop(maxHeap) if len(maxHeap) > 0 else 0