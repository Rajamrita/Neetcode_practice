from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        # Prefix product
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Postfix product
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res


# Main program
nums = [1, 2, 3, 4]

solution = Solution()

result = solution.productExceptSelf(nums)

print("Input:", nums)
print("Output:", result)