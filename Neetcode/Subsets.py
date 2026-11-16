
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision 2: Don't include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res


# Main Program
nums = [1, 2, 3]

solution = Solution()
result = solution.subsets(nums)

print("All Subsets:")
print(result)
