
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        # create hashmap and store key as number, and value as frequency
        # turn hashmap into tuples array
        # sort the tuples by values using regex
        # turn into array of only keys in the same order of the sorted array
        # return k amount of keys of the most freq
        
        hashmap = {}
        
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
            
        freq_list = list(hashmap.items())
        
        freq_list.sort(reverse = False, key = lambda x: x[1])
        
        solution = [i[0] for i in freq_list][-k:]
        return solution