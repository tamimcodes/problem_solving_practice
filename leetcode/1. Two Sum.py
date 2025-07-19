# 1. Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in my_map:
                return [i,my_map[diff]]
            my_map[value] = i
        return []
