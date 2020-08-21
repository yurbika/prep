/**
 * @param {string} S
 * @return {string}
 */
var removeOuterParentheses = function (S) {
  let balance = 0;
  let p = 0;
  let solution = [];
  for (let i = 0; i < S.length; i++) {
    if (S[i] == "(") balance++;
    else if (S[i] == ")") balance--;
    if (balance == 0) {
      solution.push(S.slice(p + 1, i));
      p = i + 1;
    }
  }
  return solution.join("");
};
