/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    hashTable = new Map()
    
    for(let i = 0; i <= strs.length - 1; i++){
        sortedString = strs[i].split('').sort().join('')
        
        //console.log(strs[i])
        //console.log(sortedString)
        //console.log(hashTable)
        
        if (hashTable[sortedString]) {
            hashTable[sortedString].push(strs[i])
        } else {
            hashTable[sortedString] = [strs[i]]
        }
        
        
        
    }
    
    return Object.values(hashTable)
    
};