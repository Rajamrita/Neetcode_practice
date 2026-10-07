from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:

            # Width between the two lines
            width = right - left

            # Water height = smaller of the two lines
            current_height = min(heights[left], heights[right])

            # Calculate water
            current_water = width * current_height

            # Store maximum water
            max_water = max(max_water, current_water)

            # Move the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water


# Main Program
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

solution = Solution()
answer = solution.maxArea(heights)

print("Heights:", heights)
print("Maximum Water:", answer)