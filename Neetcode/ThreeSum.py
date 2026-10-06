from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Fix one number
        for i, a in enumerate(nums):

            # If a is already positive,
            # we cannot make sum 0
            if a > 0:
                break

            # Skip duplicate first numbers
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1

                elif threeSum < 0:
                    l += 1

                else:
                    # Found three numbers whose sum is 0
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate numbers
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res


# Main Program
nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
answer = solution.threeSum(nums)

print("Input:", nums)
print("Three Sum:", answer)