class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for char in s:
            if 65 <= ord(char) <= 90:
                lower_num = ord(char) + 32
                result += chr(lower_num)
            else:
                result += char
        
        return result
            
        