class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i
nums = [3, 4, 5, 6]
target = 7
solution = Solution()
result = solution.twoSum(nums, target)
print(result)