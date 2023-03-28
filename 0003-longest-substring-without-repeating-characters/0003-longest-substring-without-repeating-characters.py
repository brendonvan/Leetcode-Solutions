class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        l = 0
        solution = 0
        
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            solution = max(solution, r - l + 1)
            
        return solution