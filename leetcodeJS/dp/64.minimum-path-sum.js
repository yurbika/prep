/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function (A) {
  if (!A || !A.length) return 0;
  for (let i = 0; i < A.length; i++) {
    for (let j = 0; j < A[i].length; j++) {
      if (i > 0 && j > 0) A[i][j] += Math.min(A[i - 1][j], A[i][j - 1]);
      else if (j > 0 && i <= 0) A[i][j] += A[i][j - 1];
      else if (j <= 0 && i > 0) A[i][j] += A[i - 1][j];
    }
  }
  return A[A.length - 1][A[0].length - 1];
};
