/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function (x, n) {
  if (n === 0) return 1;
  if (n === 1) return x;
  if (x === 0) return 0;
  if (x === 1) return 1;
  if (x === -1 && n < 0) return 1;
  if (x === -1 && n > 0) return -1;
  let solution = x;
  let temp = n;
  if (n < 0) temp *= -1;
  while (temp !== 1) {
    solution *= x;
    temp--;
  }

  if (n < 0) return 1 / solution;
  return solution;
};

//better version log n time

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */

var myPow = function (x, n) {
  if (n === 0) return 1;

  let pow = Math.abs(n);

  let result =
    pow % 2 === 0 ? myPow(x * x, pow / 2) : myPow(x * x, (pow - 1) / 2) * x;

  return n < 0 ? 1 / result : result;
};
