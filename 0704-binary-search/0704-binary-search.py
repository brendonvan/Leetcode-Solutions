class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        middle = int(len(nums) / 2)
        
        if target >= nums[middle]:
            for i,n in enumerate(nums[middle::]):
                if target == n:
                    return i + middle
            return -1
        if target < nums[middle]:
            for i,n in enumerate(nums[:middle]):
                if target == n:
                    return i
            return -1    
            
        