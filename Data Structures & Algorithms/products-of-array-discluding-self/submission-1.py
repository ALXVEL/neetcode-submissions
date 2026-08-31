class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        postfix = [1]

        for n in range(0, len(nums) - 1):
            prefix.append(nums[n] * prefix[n])

        print(f'prefix: {prefix}')

        i = 0
        for n in range(len(nums)-1, 0, -1):
            postfix.append(nums[n] * postfix[i])
            i+=1
        
        postfix = list(reversed(postfix))
        print(f'postfix: {postfix}')

        res = []
        for i in range(0, len(postfix)):
            res.append(postfix[i] * prefix[i])
        
        print(f'res: {res}')
        return res