class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_value_pair = {}
        for i in range(len(nums)):
            index_value_pair[nums[i]] = i
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in index_value_pair and index_value_pair[target_num]!= i:
                return [i, index_value_pair[target_num]]


        
    

        