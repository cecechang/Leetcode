class Solution(object):
    def uniquePaths(self, m, n):
        def level(num):
            if num <=1:
                return 1
            return num * level(num-1)
        return level(n+m-2)/(level(n-1)*level(m-1))