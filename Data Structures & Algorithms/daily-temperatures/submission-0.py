class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        track = {}
        ans = {}
        stack = []

        for index, value in enumerate(temperatures):
            print(f'stack: {stack} // track: {track} // ans: {ans}')
            if stack: 
                while stack and value > track[stack[-1]]:
                    ans[stack[-1]] = index - stack[-1]
                    stack.pop()
            stack.append(index)
            track[index] = value
        
        if stack:
            for n in stack:
                ans[n] = 0 

        res = []
        for n in range(0, len(ans)):
            res.append(ans[n])
        
        return res
