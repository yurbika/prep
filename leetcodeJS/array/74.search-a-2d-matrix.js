/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  if (matrix.length === 0 || !matrix) return false;
  let i = 0;
  let j = matrix[i].length - 1;
  while (i < matrix.length && j > -1) {
    if (matrix[i][j] === target) return true;
    else if (i + 1 < matrix.length && matrix[i + 1][j] <= target) i++;
    else {
      j--;
    }
  }
  return false;
};
