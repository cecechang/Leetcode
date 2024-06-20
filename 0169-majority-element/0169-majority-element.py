class Solution(object):
    def majorityElement(self, nums):
        hashtable = {}
        for num in nums:
            if num in hashtable:
                hashtable[num]+=1
            else:
                hashtable[num]=1
        for num in nums:
            if hashtable[num] > len(nums)/2:
                return num