/**
 * @param {number} A
 * @param {number} B
 * @return {string}
 */
const helper = (a, b, c1, c2) => {
  let solution = [];
  while (a || b) {
    if (a - b >= 2) {
      solution.push(c1 + c1);
      a -= 2;
      if (b) {
        solution.push(c2);
        b--;
      }
    } else {
      solution.push(c1);
      a--;
      if (b) {
        solution.push(c2);
        b--;
      }
    }
  }
  return solution.join("");
};

var strWithout3a3b = function (A, B) {
  let solution = [];
  if (A === B) return new Array(A).fill("ab").join("");
  if (A > B) {
    return helper(A, B, "a", "b");
  } else {
    return helper(B, A, "b", "a");
  }
};
