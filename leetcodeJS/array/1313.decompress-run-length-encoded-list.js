/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function (nums) {
  let solution = [];
  for (let i = 1; i < nums.length; i += 2) {
    j = nums[i - 1];
    while (j > 0) {
      solution.push(nums[i]);
      j--;
    }
  }
  return solution;
};
