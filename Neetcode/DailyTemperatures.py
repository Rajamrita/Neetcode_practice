
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores indices

        for i, t in enumerate(temperatures):

            while stack and t > temperatures[stack[-1]]:
                stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx

            stack.append(i)

        return res


# Main Program
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

solution = Solution()
result = solution.dailyTemperatures(temperatures)

print("Input:", temperatures)
print("Output:", result)
