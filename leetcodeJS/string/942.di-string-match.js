/**
 * @param {string} S
 * @return {number[]}
 */
var diStringMatch = function (S) {
  if (S.length === 0) return [];
  let d = S.length;
  let i = 0;
  let solution = [];
  for (let j = 0; j < S.length + 1; j++) {
    if (S[j] === "D") {
      solution.push(d);
      d--;
    } else {
      solution.push(i);
      i++;
    }
  }
  return solution;
};
