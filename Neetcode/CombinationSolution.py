
from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur: List[int], total: int) -> None:

            # Target reached
            if total == target:
                res.append(cur[:])
                return

            # Stop searching
            if i == len(nums) or total > target:
                return

            # Choice 1: Include current number again
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()

            # Choice 2: Skip current number
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


# Main Program
nums = [2, 3, 6, 7]
target = 7

solution = Solution()
result = solution.combinationSum(nums, target)

print("Input:", nums)
print("Target:", target)
print("Combination Sum:", result)
