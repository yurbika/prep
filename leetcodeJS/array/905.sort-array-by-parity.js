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
