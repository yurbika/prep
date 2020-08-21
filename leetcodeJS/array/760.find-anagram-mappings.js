/**
 * @param {number[]} A
 * @param {number[]} B
 * @return {number[]}
 */
var anagramMappings = function (A, B) {
  solution = [];
  for (i of A) {
    solution.push(B.indexOf(i));
  }
  return solution;
};
