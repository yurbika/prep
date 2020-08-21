/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function (moves) {
  let origin = [0, 0];
  for (i of moves) {
    if (i == "U") origin[0]++;
    else if (i == "D") origin[0]--;
    else if (i == "L") origin[1]--;
    else if (i == "R") origin[1]++;
  }
  return origin[0] == 0 && origin[1] == 0;
};
