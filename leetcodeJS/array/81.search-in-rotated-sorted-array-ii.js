/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */

var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left <= right) {
    let mid = Math.floor((right + left) / 2);

    if (nums[mid] === target) return true;

    if (nums[mid] === nums[right]) right--;
    else if (nums[mid] < nums[right]) {
      if (target > nums[mid] && target <= nums[right]) left = mid + 1;
      else right = mid;
    } else {
      if (target > nums[mid] || target < nums[left]) left = mid + 1;
      else right = mid;
    }
  }
  return false;
};
