class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ex. [1,2,4,6]
        # prefix: [1,1,2,8]
        # postfix: [48,24,6,1]

        prefix = [1]
        product = 1
        for i in range(0, len(nums) - 1):
            product *= nums[i]
            prefix.append(product)

        # debug
        print(f'prefix: {prefix}')

        postfix = [1]
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            postfix.append(product)
        
        # debug
        print(f'postfix: {postfix}')
        
        ans = []
        for i in range(0, len(nums)):
            ans.append(prefix[i] * postfix[-i - 1])
        
        return ans