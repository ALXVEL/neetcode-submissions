class Solution:
    def isPalindrome(self, s: str) -> bool:

        ptr1 = 0
        ptr2 = len(s) - 1

        s = s.lower()

        while ptr1 < ptr2:

            print(f'Checking: left: {s[ptr1]} // right: {s[ptr2]}')

            if not s[ptr1].isalnum():
                ptr1+=1
            elif not s[ptr2].isalnum():
                ptr2-=1
            else:
                if s[ptr1] != s[ptr2]:
                    return False
                ptr1+=1
                ptr2-=1
        
        return True