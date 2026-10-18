from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]


# Main Program
nums = [3, 4, 5, 1, 2]

solution = Solution()
answer = solution.findMin(nums)

print("Array:", nums)
print("Minimum Element:", answer)