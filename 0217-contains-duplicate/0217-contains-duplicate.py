class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums_set)== len(nums):
            return False
        return True
        
        