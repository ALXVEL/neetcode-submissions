class Solution:
    def trap(self, height: List[int]) -> int:
        Left, Right = 0, len(height) - 1
        maxLeft = float('-inf')
        maxRight = float('-inf')
        tap = 0

        while Left < Right:
            if height[Left] < height[Right]:
                if height[Left] >= maxLeft:
                    maxLeft = height[Left]
                else:
                    tap += maxLeft - height[Left]
                Left+=1
            else:
                if height[Right] >= maxRight:
                    maxRight = height[Right]
                else:
                    tap += maxRight - height[Right]
                Right-=1

                
        return tap