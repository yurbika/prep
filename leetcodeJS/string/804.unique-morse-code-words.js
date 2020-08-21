/**
 * @param {string[]} words
 * @return {number}
 */
var uniqueMorseRepresentations = function (words) {
  if (words == []) return 0;
  let code = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
  ];
  let solution = [];
  for (i of words) {
    s = "";
    for (j of i) {
      s += code[j.charCodeAt(j[0]) - 97];
    }
    if (!solution.includes(s)) solution.push(s);
  }
  return solution.length;
};
