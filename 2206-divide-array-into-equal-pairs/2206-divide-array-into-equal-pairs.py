class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = {}
        for num in nums:
            if num in store:
                store[num] += 1
            else:
                store[num] = 1

        for num in store:
            if store[num] % 2 != 0:
                return False
        return True
                

        