# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        product = [1]*l

        prefix = 1
        for i in range(l):
            product[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(l-1,-1,-1):
            product[i] = product[i] * postfix
            postfix = postfix * nums[i]
        
        return product

        
