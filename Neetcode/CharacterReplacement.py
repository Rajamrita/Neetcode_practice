class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        max_freq = 0

        for right in range(len(s)):

            # Frequency of current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency character in the window
            max_freq = max(max_freq, count[s[right]])

            # Number of characters we need to replace
            replacements = (right - left + 1) - max_freq

            # If replacements > k, shrink window
            if replacements > k:
                count[s[left]] -= 1
                left += 1

            # Store maximum window length
            res = max(res, right - left + 1)

        return res


# Main Program
s = "AABABBA"
k = 1

solution = Solution()
answer = solution.characterReplacement(s, k)

print("String:", s)
print("K:", k)
print("Longest Length:", answer)