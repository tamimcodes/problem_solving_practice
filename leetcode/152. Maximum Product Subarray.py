# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l= len(nums)
        ans = -10000
        prefix = 1
        suffix = 1
        for i in range(l):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix = prefix * nums[i]
            suffix = suffix * nums[l-1-i]
            ans = max(ans,max(suffix,prefix))
        return ans
