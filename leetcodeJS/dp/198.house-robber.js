/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 0) return null;
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  let dp = [];
  dp.push(nums[0]);
  dp.push(Math.max(nums[0], nums[1]));
  for (let i = 2; i < nums.length; i++) {
    dp.push(Math.max(dp[i - 1], nums[i] + dp[i - 2]));
  }
  return dp[dp.length - 1];
};
