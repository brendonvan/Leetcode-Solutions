class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # key: number    value: frequency
#         hashMap = {}
        
#         for num in nums:
#             hashMap[num] = hashMap.get(num, 0) + 1
        
#         return list(dict(sorted(hashMap.items(), key=lambda x:x[1])))[-k:]
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        # O(n)