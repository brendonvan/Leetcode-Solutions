class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create a window of the length of s1
        # move it along s2 string
        # create hmap() for s1 and the current window 
        
        if len(s1) > len(s2):
            return False
        
        s1_hmap = {}
        
        for n in s1:
            if n not in s1_hmap:
                s1_hmap[n] = 1
            else:
                s1_hmap[n] += 1
    
        l = 0
        r = 0
        length = len(s2) - 1
        
        while r <= length:
            r = l + len(s1)
            s2_hmap = {}
            for i in range(l, r):
                if s2[i] not in s2_hmap:
                    s2_hmap[s2[i]] = 1
                else:
                    s2_hmap[s2[i]] += 1
            if s1_hmap == s2_hmap:
                return True
            
            l += 1
            
        return False
            
            
                