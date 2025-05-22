from heapq import heappush, heappop
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda q: q[0]) 

        n = len(nums)
        delta = [0] * (n + 1)
        heap = []

        operations = 0
        q_index = 0

        for i, val in enumerate(nums):
            operations += delta[i] 

            while q_index < len(queries) and queries[q_index][0] == i:
                heappush(heap, -queries[q_index][1])
                q_index += 1

            while operations < val and heap and -heap[0] >= i:
                end = -heappop(heap)
                operations += 1
                delta[end + 1] -= 1  

            if operations < val:
                return -1

        return len(heap)