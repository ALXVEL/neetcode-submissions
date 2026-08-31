class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        res = [0] * len(nums) * 2

        mid = int(len(res) / 2)

        for i in range(0, len(nums)):

            print(f'Check mid: {mid}')

            res[i] = nums[i]
            res[mid] = nums[i]
            mid+=1
        
        return res
