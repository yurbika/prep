/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  let arr = {};
  while (nums.length) {
    let num = nums.shift();
    if (!arr[num]) arr[num] = 1;
    else arr[num] += 1;
  }
  for (let i in arr) {
    if (arr[i] === 1) return i;
  }
};

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
  return Math.floor(
    (3 * [...new Set(nums)].reduce((a, b) => a + b) -
      nums.reduce((a, b) => a + b)) /
      2
  );
};
