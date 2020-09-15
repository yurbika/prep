/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function (s) {
  if (s.length === 0) return "";
  let arr = s.split(" ");

  for (let i = 0; i < arr.length; i++) {
    arr[i] = [...arr[i]].reverse().join("");
  }

  let solution = arr.shift();
  while (arr.length !== 0) solution += " " + arr.shift();

  return solution;
};
