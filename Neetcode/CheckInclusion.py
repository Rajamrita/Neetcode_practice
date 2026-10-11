class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is longer, permutation is impossible
        if len(s1) > len(s2):
            return False

        # Frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Count characters of s1
        # and first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        # Check first window
        if s1_count == s2_count:
            return True

        # Sliding window
        left = 0

        for right in range(len(s1), len(s2)):

            # Add new character
            s2_count[ord(s2[right]) - ord("a")] += 1

            # Remove old character
            s2_count[ord(s2[left]) - ord("a")] -= 1

            left += 1

            # Compare frequencies
            if s1_count == s2_count:
                return True

        return False


# Main Program
s1 = "ab"
s2 = "eidbaooo"

solution = Solution()
answer = solution.checkInclusion(s1, s2)

print("s1:", s1)
print("s2:", s2)
print("Permutation exists:", answer)