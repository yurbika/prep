/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
  const table = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M",
  };
  const nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  let solution = "";
  let i = 0;
  while (num !== 0) {
    if (nums[i] <= num) {
      let r = Math.floor(num / nums[i]);
      num -= nums[i] * r;
      solution += table[nums[i]].repeat(r);
    }
    i++;
  }
  return solution;
};
