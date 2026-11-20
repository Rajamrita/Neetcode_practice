
from typing import List


class Solution:

    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:

        candidates.sort()
        res = []
        path = []

        def backtrack(start: int, remaining: int) -> None:

            # Target reached
            if remaining == 0:
                res.append(path.copy())
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Stop if number is greater than remaining target
                if candidates[i] > remaining:
                    break

                # Include current number
                path.append(candidates[i])

                # Move to next index (cannot reuse same element)
                backtrack(i + 1, remaining - candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, target)
        return res


# Main Program
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

solution = Solution()
result = solution.combinationSum2(candidates, target)

print("Candidates:", candidates)
print("Target:", target)
print("Combination Sum II:", result)
