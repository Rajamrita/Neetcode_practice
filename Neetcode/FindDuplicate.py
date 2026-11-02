
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find duplicate number
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


# Main Program
nums = [1, 3, 4, 2, 2]

solution = Solution()
result = solution.findDuplicate(nums)

print("Duplicate number:", result)
