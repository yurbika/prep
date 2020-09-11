/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  if (nums.length === 0) return 0;
  let solution = 1;
  for (let i = 0; i < nums.length; i++) {
    if (nums.indexOf(nums[i] - 1) === -1) {
      let j = 1;
      let temp = 1;
      while (nums.indexOf(nums[i] + j) !== -1) {
        temp++;
        j++;
      }
      if (temp > solution) solution = temp;
    }
  }
  return solution;
};
