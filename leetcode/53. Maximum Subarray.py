# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(cur_sum,max_sum)
            
            if cur_sum <0:
                cur_sum = 0
        
        return max_sum
