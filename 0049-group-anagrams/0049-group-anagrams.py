class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = {}
        
        for string in strs:
            sortedString = ''.join(sorted(string))
            print(sortedString)
            
            if sortedString in Anagrams:
                Anagrams[sortedString].append(string)
            
            else: Anagrams[sortedString] = [string]
        
        return list(Anagrams.values())