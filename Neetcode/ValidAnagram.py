class Solution:

    def isAnagram(self, s, t):

        # If lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False

        # 26 letters: a to z
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        # Check if all counts are zero
        for c in count:
            if c != 0:
                return False

        return True


# Main program
s = "anagram"
t = "nagaram"

solution = Solution()

result = solution.isAnagram(s, t)

print(result)