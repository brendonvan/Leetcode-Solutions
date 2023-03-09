class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: number    value: frequency
        hashMap = {}
        
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        
        return list(dict(sorted(hashMap.items(), key=lambda x:x[1], reverse=False)))[-k:]