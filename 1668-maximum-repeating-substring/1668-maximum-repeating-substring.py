class Solution(object):
    def maxRepeating(self, sequence, word):
        count = 0
        while True:
            if count * word not in sequence:
                return count-1
            count +=1
        
        