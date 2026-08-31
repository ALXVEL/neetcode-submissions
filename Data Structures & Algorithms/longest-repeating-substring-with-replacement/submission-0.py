class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}

        Left = 0
        maxC = 0
        for Right in range(0, len(s)):
            if s[Right] in count:
                count[s[Right]] += 1
            else:
                count[s[Right]] = 1
            maxC = max(maxC, count[s[Right]])

            if (Right - Left + 1) - maxC > k:
                count[s[Left]] -= 1
                Left += 1
        
        return Right - Left + 1