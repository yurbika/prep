/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  if (s.length === 0) return "";
  let table = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
  let solution = table[s[s.length - 1]];
  let i = s.length - 2;
  while (i !== -1) {
    if (table[s[i]] < table[s[i + 1]]) solution -= table[s[i]];
    else {
      solution += table[s[i]];
    }
    i--;
  }
  return solution;
};
