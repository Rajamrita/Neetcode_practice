class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
nums = [1, 2, 3, 4, 5, 1]
solution = Solution()
result = solution.hasDuplicate(nums)
print(result)  # Output: True

