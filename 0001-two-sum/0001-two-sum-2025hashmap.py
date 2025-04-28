class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in hashmap and hashmap[target_num] != i:
                return [i, hashmap[target_num]]
        
        