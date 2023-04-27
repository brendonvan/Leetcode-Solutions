class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hset = set()
        for n in nums:
            if n in hset:
                return n
            hset.add(n)