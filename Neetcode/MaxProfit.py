class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right

            right += 1

        return max_profit


# Test
prices = [7, 1, 5, 3, 6, 4]

solution = Solution()
print(solution.maxProfit(prices))