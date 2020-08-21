/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function (nums) {
  if (nums == [] || nums.length == 1) return nums;
  let p1 = 0;
  let p2 = 1;
  let solution = [];
  let cnt = 0;
  while (p1 < nums.length) {
    if (nums[p1] > nums[p2]) cnt++;
    if (p2 < nums.length) p2++;
    else {
      solution.push(cnt);
      cnt = 0;
      p1++;
      p2 = 0;
    }
  }
  return solution;
};
