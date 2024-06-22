class Solution(object):
    def findTheDifference(self, s, t):
        for char in t:
            if char not in s:
                return char
        