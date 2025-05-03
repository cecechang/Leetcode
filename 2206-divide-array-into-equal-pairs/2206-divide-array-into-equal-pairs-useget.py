class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            store[num] = store.get(num, 0) + 1

        for count in store:
            if store[count] % 2 != 0:
                return False
        return True
                

        
