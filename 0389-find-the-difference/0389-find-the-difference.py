class Solution(object):
    def findTheDifference(self, s, t):
        t_list = [char for char in t]
        for char in s:
            t_list.remove(char)
        
        return t_list[0]
        