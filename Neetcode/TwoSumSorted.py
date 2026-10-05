from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            elif current_sum < target:
                left += 1

            else:
                right -= 1

        return []


# -------------------------
# Main Program
# -------------------------

numbers = [2, 7, 11, 15]
target = 9

solution = Solution()

answer = solution.twoSum(numbers, target)

print("Numbers:", numbers)
print("Target:", target)
print("Answer:", answer)