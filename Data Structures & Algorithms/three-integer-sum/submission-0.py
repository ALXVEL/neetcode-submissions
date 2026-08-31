class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        this_dict = {}

        for index, value in enumerate(nums):
            this_dict[value] = index

        sol = []
        check = []
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                res = - (nums[i] + nums[j])
                if res in this_dict:
                    if i != j and j != this_dict[res] and i != this_dict[res]:
                        if sorted([nums[i], nums[j], res]) not in check:
                            sol.append([nums[i], nums[j], res])
                            check.append(sorted([nums[i], nums[j], res]))

        return sol