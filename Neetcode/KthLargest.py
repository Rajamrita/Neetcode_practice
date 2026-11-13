
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap)

        # Keep only k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]


# Main Program
k = 3
nums = [4, 5, 8, 2]

obj = KthLargest(k, nums)

print(obj.add(3))   # Add 3
print(obj.add(5))   # Add 5
print(obj.add(10))  # Add 10
print(obj.add(9))   # Add 9
print(obj.add(4))   # Add 4
