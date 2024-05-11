class Solution(object):
    def mySqrt(self, x):
        low = 1
        high = x
        while low <= high:
            mid = (low+high)//2
            if x == mid * mid:
                return mid
            if x > mid * mid:
                low = mid +1
            else: high = mid - 1
        return low-1
        
        