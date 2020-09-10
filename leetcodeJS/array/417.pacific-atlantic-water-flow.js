/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */

const dfs = (matrix, row, col, ocean, prev) => {
  if (row < 0 || col < 0 || row >= matrix.length || col >= matrix[0].length)
    return;
  if (ocean[row][col] === -1) return;
  if (matrix[row][col] < prev) return;

  ocean[row][col] = -1;
  dfs(matrix, row + 1, col, ocean, matrix[row][col]);
  dfs(matrix, row - 1, col, ocean, matrix[row][col]);
  dfs(matrix, row, col + 1, ocean, matrix[row][col]);
  dfs(matrix, row, col - 1, ocean, matrix[row][col]);
};

var pacificAtlantic = function (matrix) {
  if (matrix.length === 0) return [];
  const pacific = [];
  const atlantic = [];

  for (let i = 0; i < matrix.length; i++) {
    pacific[i] = Array(matrix[0].length).fill(0);
    atlantic[i] = Array(matrix[0].length).fill(0);
  }

  for (let i = 0; i < matrix[0].length; i++) {
    //col
    dfs(matrix, 0, i, pacific, Number.MIN_SAFE_INTEGER);
    dfs(matrix, matrix.length - 1, i, atlantic, Number.MIN_SAFE_INTEGER);
  }

  for (let i = 0; i < matrix.length; i++) {
    //row
    dfs(matrix, i, 0, pacific, Number.MIN_SAFE_INTEGER);
    dfs(matrix, i, matrix[0].length - 1, atlantic, Number.MIN_SAFE_INTEGER);
  }

  let solution = [];

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (pacific[i][j] === -1 && pacific[i][j] === atlantic[i][j])
        solution.push([i, j]);
    }
  }

  return solution;
};
