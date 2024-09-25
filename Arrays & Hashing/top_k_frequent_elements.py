from collections import Counter
from heapq import heapify,heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums=Counter(nums)
        heap=[(-count,val) for val,count in nums.items()]
        heapify(heap)
        result=[]
        for i in range(k):
            result.append(heappop(heap)[1])
        return result