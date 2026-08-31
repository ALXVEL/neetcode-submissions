class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        # sort 
        sorted_nums = sorted(nums)

        # set
        set_nums = sorted(set(sorted_nums))

        print(f'set_nums: {set_nums}')

        # check for consecutive (max)
        max_count = 1
        count = 1
        for i in range(0, len(set_nums)):

            if i == 0:
                continue
            
            check = set_nums[i] - set_nums[i-1]
            print(f'Check: {set_nums[i]} - {set_nums[i-1]} = {check}')

            if abs(check) == 1:
                count += 1
            else:
                count = 1
            
            max_count = max(max_count, count)

        return max_count