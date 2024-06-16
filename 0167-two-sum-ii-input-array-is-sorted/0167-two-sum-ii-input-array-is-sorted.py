class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r= len(numbers)-1
        while l < r:
            if target - numbers[r] == numbers[l]:
                return [l+1, r+1]
            elif target - numbers[r] > numbers[l]:
                l+=1
            else:
                r-=1
        
        