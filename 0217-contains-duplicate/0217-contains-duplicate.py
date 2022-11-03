class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # I like to start with the brute force solution first and then optimizing it later
        
        # Go through each number in array. 
        # Each time you check a number, check if the original array contains a duplicate element.
        # for idx, num in enumerate(nums): 
        #     numsCopy = nums.copy()
        #     numsCopy.pop(idx)
        #     if num in numsCopy:
        #         return True
        # return False

        # To optimize it I would:
        # use a hashset to store a number if it doesn't exist, if it does return True

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            else:
                hashset.add(n)
        return False


        # I know a quick one-liner for this question it looks like this:

        # return len(nums) != len(set(nums))