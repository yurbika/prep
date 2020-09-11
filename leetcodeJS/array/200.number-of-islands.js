/**
 * @param {character[][]} grid
 * @return {number}
 */

const helper = (grid, row, col) => {
  if (row < 0 || col < 0 || col >= grid[0].length || row >= grid.length) return;
  if (grid[row][col] !== "1") return;

  grid[row][col] = "0";
  helper(grid, row + 1, col);
  helper(grid, row - 1, col);
  helper(grid, row, col + 1);
  helper(grid, row, col - 1);
};

var numIslands = function (grid) {
  if (grid.length === 0) return 0;
  let cnt = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] !== "1") continue;
      helper(grid, i, j);
      cnt++;
    }
  }

  return cnt;
};
