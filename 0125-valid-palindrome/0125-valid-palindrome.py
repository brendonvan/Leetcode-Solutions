import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        #ADjusting string to the final form without space or comma
        left = 0
        print(len(s))
        right =  len(s) -1
        #Initializing two pointer P1 and P2 point to the left-most side and the right-most 
        while left <right:
        #Moving two pointers in and compare two pointers if one case does not match then know that string is not a palindrom
            if s[left] != s[right]:
                return False
            left +=1
            right -=1
        return True