/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  if (nums.length === 0) return 0;
  let solution = Number.NEGATIVE_INFINITY;
  let temp = Number.NEGATIVE_INFINITY;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > temp + nums[i]) temp = nums[i];
    else {
      temp += nums[i];
    }
    if (temp > solution) solution = temp;
  }

  return solution;
};
