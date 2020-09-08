/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  for (let i = 0; i < nums.length - 2; i++) {
    let j = i + 1;
    let k = i + 2;
    if (nums[i] === nums[j] && nums[i] === nums[k]) {
      nums.splice(i, 1);
      i--;
    }
  }
  return nums.length;
};
