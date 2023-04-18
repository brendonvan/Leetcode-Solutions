class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create hash set to make sure there's no repeating characters
        # if next character is in hashset reset window and compare current window to longest substring
        
        hset = set()
        l = 0
        longest = 0
        
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            longest = max(longest, r - l + 1)
                
            
        return longest