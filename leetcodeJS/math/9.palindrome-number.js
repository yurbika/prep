/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  if (x < 0) return false;
  if (x < 10) return true;
  let temp = [];
  while (x >= 1) {
    temp.push(x % 10);
    x = Math.floor(x / 10);
  }
  for (let i = 0; i < temp.length / 2; i++) {
    if (temp[i] !== temp[temp.length - 1 - i]) return false;
  }
  return true;
};
