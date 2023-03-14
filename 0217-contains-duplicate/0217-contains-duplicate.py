class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
        
#         for num in nums:
#             if num in hset:
#                 return True
#             else:
#                 hset.add(num)
        
#         return False