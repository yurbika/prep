/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function (A) {
  let solution = [];
  for (i of A) {
    if (i % 2 == 0) solution.unshift(i);
    else {
      solution.push(i);
    }
  }
  return solution;
};

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function (A) {
  if (A.length === 0 || A.length === 1) return A;
  let left = 0;
  let right = A.length - 1;
  while (left < right) {
    if (A[left] % 2) [A[left], A[right]] = [A[right], A[left]];

    if (A[left] % 2 === 0) left++;
    if (A[right] % 2 === 1) right--;
  }
  return A;
};
