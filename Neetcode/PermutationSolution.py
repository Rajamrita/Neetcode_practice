
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)

        def backtrack():

            # Base case
            if len(path) == len(nums):
                res.append(path[:])
                return

            # Try every number
            for i in range(len(nums)):

                if used[i]:
                    continue

                # Choose the number
                used[i] = True
                path.append(nums[i])

                # Explore next position
                backtrack()

                # Backtrack: undo the choice
                path.pop()
                used[i] = False

        backtrack()
        return res


# Main Program
nums = [1, 2, 3]

solution = Solution()
result = solution.permute(nums)

print("Input:", nums)
print("All Permutations:")
print(result)
print("Total Permutations:", len(result))
