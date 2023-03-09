/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let hset = new Set(nums);
    return hset.size !== nums.length
};