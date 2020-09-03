/**
 * @param {number[]} nums
 * @return {number[][]}
 */

function isArrayInArray(arr, item) {
  var item_as_string = JSON.stringify(item);

  var contains = arr.some(function (ele) {
    return JSON.stringify(ele) === item_as_string;
  });
  return contains;
}

const wave = (num, arr) => {
  let copyArr = [...arr];
  for (let i = 0; i < arr.length; i++) {
    let temp = copyArr[i].slice();
    temp.push(num);
    temp.sort((a, b) => a - b);
    if (!isArrayInArray(copyArr, temp)) copyArr.push(temp);
  }
  return copyArr;
};

const helper = (nums, memo) => {
  if (nums.length === 1) {
    return wave(nums[0], memo);
  }

  let num = nums.pop();
  memo = wave(num, helper(nums, memo));
  return memo;
};

var subsetsWithDup = function (nums) {
  if (nums.length === 0) return [];
  if (nums.length === 1) return [[], nums];
  let memo = [[]];
  memo = helper(nums, memo);

  return memo;
};
