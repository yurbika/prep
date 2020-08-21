var runningSum = function (nums) {
  if (nums == []) return null;
  let arr = [nums[0]];

  for (let i = 1; i < nums.length; i++) {
    let cnt = nums.slice(0, i + 1).reduce((acc, val) => acc + val);
    arr.push(cnt);
  }
  return arr;
};
