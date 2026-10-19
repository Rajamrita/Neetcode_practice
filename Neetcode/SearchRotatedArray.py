from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Check if left half is sorted
            if nums[l] <= nums[mid]:

                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


# Main Program
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

solution = Solution()
answer = solution.search(nums, target)

print("Array:", nums)
print("Target:", target)
print("Index:", answer)