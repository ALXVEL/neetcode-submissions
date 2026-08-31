class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFix = []
        postFix = []

        product = 1
        for n in nums:
            preFix.append(product)
            product *= n
            
        
        product = 1
        for n in reversed(nums):
            postFix.append(product)
            product *= n
            

        postFix.reverse()

        res = []
        for i in range(0, len(nums)):
            res.append(preFix[i] * postFix[i])
        
        return res

        