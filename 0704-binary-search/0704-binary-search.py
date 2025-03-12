class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        h = len(nums) - 1
        l = 0

        while l <= h:
            mid = (h+l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                h = mid -1
            elif target > nums[mid]:
                l = mid +1
        return -1

