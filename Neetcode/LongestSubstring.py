class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()

        l = 0
        res = 0

        for r in range(len(s)):

            # If duplicate character is found
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            # Add current character
            char_set.add(s[r])

            # Calculate current window length
            res = max(res, r - l + 1)

        return res


# Main Program
s = "abcabcbb"

solution = Solution()
answer = solution.lengthOfLongestSubstring(s)

print("String:", s)
print("Longest Substring Length:", answer)