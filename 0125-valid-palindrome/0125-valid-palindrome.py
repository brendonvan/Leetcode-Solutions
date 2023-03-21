class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # remove spaces, capitals, etc
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        
        pointer_one = 0
        pointer_two = len(s) - 1
        
        while pointer_one < pointer_two:
            
            if s[pointer_one] != s[pointer_two]:
                return False
            
            pointer_one += 1
            pointer_two -= 1
        
        return True