class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        ans = []
        for ptr in range(0, len(nums)):
            if ptr >= 1 and nums[ptr] == nums[ptr-1]:
                continue
            
            Left, Right = ptr+1, len(nums) - 1
            while Left < Right:
                print(f"ptr: {nums[ptr]} // left: {nums[Left]} // right: {nums[Right]}")
                if nums[ptr] + nums[Left] + nums[Right] == 0:
                    if ptr != Left and ptr != Right:
                        ans.append([nums[ptr], nums[Left], nums[Right]])
                    Left += 1
                    Right -= 1

                    while nums[Left] == nums[Left - 1] and Left < Right:
                        Left +=1
                    
                    while nums[Right] == nums[Right + 1] and Left < Right:
                        Right -=1

                elif nums[ptr] + nums[Left] + nums[Right] > 0:
                    Right -= 1
                else:
                    Left += 1
        
        return ans