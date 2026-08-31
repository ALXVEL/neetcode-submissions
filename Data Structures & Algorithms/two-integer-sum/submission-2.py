class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        


        for index,value in enumerate(nums):
            sliced_list = nums[index+1:len(nums)]
            if target - value in sliced_list:
                return [index, sliced_list.index(target-value) + index + 1]
        
        return [0,0]