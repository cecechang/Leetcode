class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        for count in store:
            if store[count] % 2 != 0:
                return False
        return True
                
                

        
