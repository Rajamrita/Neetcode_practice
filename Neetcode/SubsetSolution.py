
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # Include current element
            subset.append(nums[i])
            backtrack(i + 1)

            # Exclude current element
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res


# Main Program
nums = [1, 2, 3]

solution = Solution()
result = solution.subsets(nums)

print("Input:", nums)
print("All Possible Subsets:")
print(result)
print("Total Subsets:", len(result))
