class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for n in strs:
            res += '#&^'+ str(len(n)) + '^&#' + n
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        while i < len(s):
            if s[i] == '#' and s[i+1] == '&' and s[i+2] == '^':
                i += 3
                num = ""
                while s[i] != '^':
                    num += s[i]
                    i+=1
                i += 3
            
            print(int(num))
            count = 0
            
            arr = ""
            while count < int(num):
                arr += s[i]
                count += 1
                i += 1
            
            ans.append(arr)

        return ans