class Solution(object):
    def strStr(self, haystack, needle):
        word_length = len(needle)
        if word_length == 0: 
            return 0
        
        for i in range(len(haystack) - word_length + 1):
            if haystack[i:i + word_length] == needle:
                return i
        return -1 
        