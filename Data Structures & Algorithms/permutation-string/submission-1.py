class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = {}
        # Build the frequency dictionary for s1
        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        count = {}
        Left = 0
        for Right in range(len(s2)):
            # Add the current character to the count dictionary
            count[s2[Right]] = count.get(s2[Right], 0) + 1
            
            # Ensure window size matches the length of s1
            if Right - Left + 1 > len(s1):
                # Reduce the count of the leftmost character
                count[s2[Left]] -= 1
                if count[s2[Left]] == 0:
                    del count[s2[Left]]  # Remove it if count is zero
                Left += 1
            
            # Compare the count dictionary with s1_dict
            if count == s1_dict:
                return True
        
        return False