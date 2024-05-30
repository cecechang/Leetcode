class Solution(object):
    def sortedSquares(self, nums):
        squared_list = [ (n**2) for n in nums]
        return sorted(squared_list)
        