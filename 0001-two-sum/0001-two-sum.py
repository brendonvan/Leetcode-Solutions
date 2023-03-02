class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for pointer_one in range(len(nums)):
            for pointer_two in range(pointer_one):

                if (nums[pointer_one] + nums[pointer_two]) == target:
                    return [pointer_one, pointer_two]
        
