class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_dic = {}

        for index, value in enumerate(nums):
            print(f'Calculating: {target} - {value} = {target-value}' )
            diff = target - value
            
            if diff in diff_dic:
                return [diff_dic[diff], index]
            else:
                print(f'Storing: {diff} : {index}')
                diff_dic[value] = index
        
        return [0,0]