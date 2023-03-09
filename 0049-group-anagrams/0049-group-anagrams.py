class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = {}
        
        for string in strs:
            
            # makes it alphabetical
            sortedString = ''.join(sorted(string))
            
            #print(string)
            #print(sortedString)
            #print(Anagrams)
            
            # if the alphabetical order string is in hashtable
            if sortedString in Anagrams:
                Anagrams[sortedString].append(string)
            
            else: Anagrams[sortedString] = [string]
        
        return Anagrams.values()