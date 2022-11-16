class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dict = [Int: Int]()

        for (i, value) in nums.enumerated() {
            if let index = dict[target - value] {
                return [index, i]
            } else {
                dict[value] = i
            }
        }
    
        return []
    }
}