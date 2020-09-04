/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let zero = nums.filter((x) => x == 0).length;
  let one = nums.filter((x) => x == 1).length;
  let two = nums.filter((x) => x == 2).length;

  for (let i = 0; i < nums.length; i++) {
    if (zero > 0) {
      nums[i] = 0;
      zero--;
    } else if (one > 0) {
      nums[i] = 1;
      one--;
    } else {
      nums[i] = 2;
    }
  }
};

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function (nums) {
  let cur = 0;
  let left = 0;
  let right = nums.length - 1;

  while (cur <= right) {
    if (nums[cur] === 0) {
      [nums[left], nums[cur]] = [nums[cur], nums[left]];
      left++;
      cur++;
    } else if (nums[cur] === 2) {
      [nums[cur], nums[right]] = [nums[right], nums[cur]];
      right--;
    } else {
      cur++;
    }
  }
};
